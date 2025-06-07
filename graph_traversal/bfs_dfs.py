# BFS and DFS

#    Implement both BFS and DFS for directed graph.

#    bfs(n, edges) and dfs(n, edges) where nodes are 0...(n-1) and edges is a list of (u, v) pairs.

#    e.g., for the following example:

#    0 --> 1 --> 2 --> 3
#          |           v
#          +---> 4 --> 5

#    >>> bfs(6, [(0, 1), (1, 2), (2, 3), (1, 4), (4, 5), (3, 5)])
#    [0, 1, 2, 4, 3, 5]
#    >>> dfs(6, [(0, 1), (1, 2), (2, 3), (1, 4), (4, 5), (3, 5)])
#    [0, 1, 2, 3, 5, 4]

from collections import defaultdict
from collections import deque

# convert edges to adjacency list
def edges2adjlist(edges):
    adj = defaultdict(list)
    for (u, v) in edges:
        adj[u].append(v)
    return adj

def print_list(adj):
    for u in adj:
        ns_str = ", ".join(str(v) for v in adj[u])
        print(f"{u} -> [{ns_str}]")

def bfs(n, edges):
    queue = deque()
    order = []
    visited = set()
    adj = edges2adjlist(edges)

    queue.append(edges[0][0])
    visited.add(edges[0][0])
    # first in
    while queue:
        u = queue.popleft()
        order.append(u)
        for v in adj[u]:
            if v not in visited:
                visited.add(v)
                queue.append(v)
                
    return order

def dfs(n, edges):
    adj = edges2adjlist(edges)
    order = []
    visited = set()
    
    def visit(u):
        visited.add(u)
        order.append(u)
        for v in adj[u]:
            if v not in visited:
                visit(v)
    visit(edges[0][0])
    return order


if __name__ == "__main__":
    edges = [(0, 1), (1, 2), (2, 3), (1, 4), (4, 5), (3, 5)]
    n = len(edges)
    adj = edges2adjlist(edges)
    print_list(adj)
    print(bfs(n, edges))
    print(dfs(n, edges))

