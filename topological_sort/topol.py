# Topological Sort
   
#    For a given directed graph, output a topological order if it exists.
   
#    Tie-breaking: ARBITRARY tie-breaking. This will make the code 
#    and time complexity analysis a lot easier. 

#    e.g., for the following example:

#      0 --> 2 --> 3 --> 5 --> 6
#         /    \   |  /    \
#        /      \  v /      \
#      1         > 4         > 7

#    >>> order(8, [(0,2), (1,2), (2,3), (2,4), (3,4), (3,5), (4,5), (5,6), (5,7)])
#    [0, 1, 2, 3, 4, 5, 6, 7]

#    Note that order() takes two arguments, n and list_of_edges, 
#    where n specifies that the nodes are named 0..(n-1).

#    If we flip the (3,4) edge:

#    >>> order(8, [(0,2), (1,2), (2,3), (2,4), (4,3), (3,5), (4,5), (5,6), (5,7)])
#    [0, 1, 2, 4, 3, 5, 6, 7]

#    If there is a cycle, return None

#    >>> order(4, [(0,1), (1,2), (2,1), (2,3)])
#    None

#    Other cases:

#    >>> order(5, [(0,1), (1,2), (2,3), (3,4)])
#    [0, 1, 2, 3, 4]

#    >>> order(5, [])
#    [0, 1, 2, 3, 4]  # could be any order   

#    >>> order(3, [(1,2), (2,1)])
#    None

#    >>> order(1, [(0,0)]) # self-loop
#    None

#    Tie-breaking: arbitrary (any valid topological order is fine).

#    You need to implement both versions:
#    - bottom-up (BFS): order(n, edges)
#    - top-down (DFS from n-1), order2(n, edges)
from collections import defaultdict
from collections import deque

def edge2adjlist(edges):
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
    return adj

def print_adjlist(adj):
    for u in adj:
        n_str = ", ".join(str(v) for v in adj[u])
        print(f"{u} -> [{n_str}]")

# BFS topological sort (Kahn's algorithm) (BFS style approach)
def order(n, adj):
    order = []

    in_deg = [0] * n
    for u in adj:
        for v in adj[u]:
            in_deg[v] += 1

    print(in_deg) # how many edges point into x (v) u->v

    zero_in = deque()
    for u in range (0, n):
        if in_deg[u] == 0:
            zero_in.append(u)

    print(zero_in)

    while zero_in:
        u = zero_in.popleft()
        order.append(u)
        for v in adj[u]:
            in_deg[v] -= 1
            if in_deg[v] == 0:
                zero_in.append(v)

    if len(order) == n:
        return order
    else:
        return None
    

# BFS 
def _order1(n, edges): # DEFAULT SOLUTION (classical textbook style): queue and head pointer
   
    # convert list of edges to adj. list
    adjlist = defaultdict(list)
    indegree = defaultdict(int)

    for u, v in edges: # u->v
        adjlist[u].append(v)
        indegree[v] += 1
        
    queue = [u for u in range(n) if indegree[u] == 0]
    head = 0 # queue head pointer
    while head < len(queue):
        u = queue[head] # pop queue
        head += 1
        yield u # next in the topol order
        for v in adjlist[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)

# dereks solution BFS Kahn's algorithm
def _order2(n, edges):
    adjlist = defaultdict(list)
    indegrees = defaultdict(int) 

    for u, v in edges: # u -> v
        adjlist[u].append(v)
        indegrees[v]+=1   # u -> v (so by increasing for v we acoount for the indegree of the v)
        # we use dictionary for non-zero indegree
    
    # smart way to create queue
    queue = [u for u in range(0,n) if indegrees[u] == 0]

    for u in queue:
        yield u
        for v in adjlist[u]:
            indegrees[v]-=1
            if indegrees[v] == 0:
                queue.append(v)

class CycleException(Exception):
    pass

# DFS approach
def _order3(n, edges):
    prereqs = defaultdict(list)
    # adjlist = defaultdict(list)

    for u, v in edges: # build dictionary of the incoming edges from the parent verticies
        # adjlist[u].append(v)
        # Note I use prereqs as adjlist ( no need for separate adjlist)
        prereqs[v].append(u)

    for v in prereqs:
        parents_str = ", ".join([str(u) for u in prereqs[v]])
        print(f"{v} -> [{parents_str}]")
    
    out = []
    color = defaultdict(int) # 0 - white untouched, 1 - in process exploring neighbours, 2 - completely explored neighbours
    back_track = []

    def visit(v):
        if color[v] == 1:
            bt_s = " -> ".join(reversed(back_track))
            print(f"Cycle on:\n{bt_s}")
            bt_s = " -> ".join(back_track)
            print(bt_s)
            raise CycleException("cycle detected")
        
        if color[v] == 0: #white
            color[v] = 1
            back_track.append(str(v))
            for u in prereqs[v]:
                visit(u)
            color[v] = 2

            out.append(v)
            del back_track[:]

    #breakpoint()
    try: 
        for v in range(n):
            visit(v)

    except CycleException:

        print("-"*60)
        for v in prereqs:
            parents_str = ", ".join([str(u) for u in prereqs[v]])
            print(f"{v} -> [{parents_str}]")

        return out
    return out



def _order4(n, edges): # top-down, recursive, memoization

    def visit(v): # DFS
        if color[v] == 1: # gray
         
            raise CycleException("cycle detected")
        elif color[v] == 0: # white: visit (if black: return -- memoization)
            color[v] = 1 # becomes gray
            for u in prereqs[v]:
                visit(u)
            color[v] = 2 # now black; done
            out.append(v) # take this course now

    prereqs = defaultdict(list) # incoming edges
    for u, v in edges: # u->v
        prereqs[v].append(u)
    
    color = defaultdict(int) # default: white (0)
    out = [] # topological order (output)
    try:
        for u in range(n): # DFS on each non-visited node
            visit(u) # try to visit u if it's white            
    except CycleException: # important: only catch my own exception
        return out # cycle detected; out is not the whole set
    return out



if __name__ == "__main__":
    edges = [(0,2), (1,2), (2,3), (2,4), (4,3), (3,5), (4,5), (5,6), (5,7)]
    edges_cycle = [(0,2), (1,2), (2,3), (2,4), (4,3), (3,5), (5,4), (5,6), (5,7)]
    n = len(edges)-1
    adj = edge2adjlist(edges)
    print("-"*20, " Orignal Adjacency list ", "-"*20)
    print_adjlist(adj)

    # print(order(n, adj))

    print("-"*20, " Default BFS Kahn's algorithm (using head pointer) ", "-"*20)
    xs = []
    for x in _order1(n, edges):
        xs.append(str(x))
    xstr = ", ".join(xs)
    print(f"[{xstr}]")    
    
    
    print("-"*20, " Without head pointer  ", "-"*20)
    xs = []
    for x in _order2(n, edges):
        xs.append(str(x))
    xstr = ", ".join(xs)
    print(f"[{xstr}]")
   

    print("-"*20, " DFS topological sort using colors (white 0 , gray 1, black 2) ", "-"*20)
    print(_order3(n, edges_cycle))





