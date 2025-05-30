from collections import defaultdict
from collections import deque

def edges2adjlist(edges):
    adj = defaultdict(list)
    for u,v in edges:
        adj[u].append(v)
    return adj

def print_adjlist(n, edges):
    adj = edges2adjlist(edges)
    for u in range(n):
        neighbours = adj.get(u, [])
        neigbours_str = ", ".join(str(v) for v in neighbours)
        print(f"{u} -> [{neigbours_str}]") 


def bfs(edges):
    #init
    order = []
    Q = deque() #we need FIFO (queue) behavior so we need to use Deque or pop(0) but it's better to use deque
    visited = set() #visited must be set
    adj = edges2adjlist(edges)
    # start
    Q.append(edges[0][0]) # start
    visited.add(edges[0][0])
    while Q: # V + E
        u = Q.popleft()
        order.append(u)
        # for each neighbour
        for v in adj[u]:
            if v not in visited:
                visited.add(v)
                Q.append(v)
    return order

def dfs(edges):
    # inist
    order = [] # optional
    stack = [] # stack just a normal list with pop LIFO (last in first out (stack))
    visited = set()
    adj = edges2adjlist(edges)

    #start
    stack.append(edges[0][0])
    visited.add(edges[0][0])

    while stack:
        u = stack.pop()
        order.append(u)
        for v in adj[u]:
            if v not in visited:
                visited.add(v)
                stack.append(v)
    return order


def rec_dfs(edges):
    order = []
    visited = set()
    adj = edges2adjlist(edges)

    def visit(u):
        visited.add(u)
        order.append(u)
        for v in adj[u]:
            if v not in visited:
                visit(v)

    visit(edges[0][0])
    return order
              

# Test examples
if __name__ == "__main__":
    print("="*40)

    edges1 = [(0, 1), (1, 2), (0, 2)]
    edges2= [(0, 1), (1, 2), (2, 3), (1, 4), (4, 5), (3, 5), (5,6), (6,11), (5,7), (5,8), (5,9)]
    n2 = len(edges2)

    print(f"(BFS) Connected Graph: {edges2}")
    print("Adjacency list:")
    print_adjlist(n2, edges2)
    print(f"BFS order:{bfs(edges2)}")

    print("="*40)

    edges1 = [(0, 1), (1, 2), (0, 2)]
    edges2= [(0, 1), (1, 2), (2, 3), (1, 4), (4, 5), (3, 5), (5,6), (6,11), (5,7), (5,8), (5,9)]
    n2 = len(edges2)

    print(f"(DFS) Connected Graph: {edges2}")
    print("Adjacency list:")
    print_adjlist(n2, edges2)
    print(f"DFS order:{dfs(edges2)}")

    print("="*40)

    edges1 = [(0, 1), (1, 2), (0, 2)]
    edges2= [(0, 1), (1, 2), (2, 3), (1, 4), (4, 5), (3, 5), (5,6), (6,11), (5,7), (5,8), (5,9)]
    n2 = len(edges2)

    print(f"(DFS RECURSION) Connected Graph: {edges2}")
    print("Adjacency list:")
    print_adjlist(n2, edges2)
    print(f"DFS RECURSION order:{rec_dfs(edges2)}")

    print("="*40)


    