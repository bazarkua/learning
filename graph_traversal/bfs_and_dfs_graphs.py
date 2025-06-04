from collections import deque
from collections import defaultdict



def edges2list(edges):
    adj = defaultdict(list)
    for u,v in edges:
        adj[u].append(v)
    return adj

def print_adjlist(adj):
    for u in range(len(list(adj))):
        neighbours = adj.get(u, [])
        nbs_str = ', '.join(str(v) for v in neighbours)
        print(f"{u} -> [{nbs_str}]")

def bfs_color(edges):
    color = defaultdict(int)
    # (0 white) - never seen (1 gray) - discovered currently processing (2 black) - fully processed
    adj = edges2list(edges)
    order = []

    def _BFS(v):
        queue = [v]
        for u in queue:
            order.append(u)
            for w in adj[u]:
                if color[w] == 0: # if white
                    queue.append(w)
                    color[w] = 1
            color[u] = 2 # we are done

    for v in range(0, len(edges)-1):
        if color[v] == 0:
            _BFS(v)

    return order

def dfs_color(edges):
    adj = edges2list(edges)
    color = defaultdict(int)
    order = []

    def _DFS(v):
        color[v] = 1 # processing
        order.append(v)
        for w in adj[v]:
            if color[w] == 0:
                _DFS(w)
        color[v] = 2


    for v in range(0, len(edges)-1):
        if color[v] == 0:
            _DFS(v)

    return order

if __name__ == "__main__":
    print("="*40)

    edges1 = [(0, 1), (1, 2), (0, 2)]
    edges2= [(0, 1), (1, 2), (2, 3), (1, 4), (4, 5), (3, 5), (5,6), (6,11), (5,7), (5,8), (5,9)]
    
    print(f"(BFS) Connected Graph: {edges2}")
    print("Adjacency list:")
    adj = edges2list(edges2)
    print_adjlist(adj)
    print(bfs_color(edges2))

    print("="*40)

    edges1 = [(0, 1), (1, 2), (0, 2)]
    edges2= [(0, 1), (1, 2), (2, 3), (1, 4), (4, 5), (3, 5), (5,6), (6,11), (5,7), (5,8), (5,9)]

    print(f"(DFS) Connected Graph: {edges2}")
    print("Adjacency list:")
    print_adjlist(adj)
    print(f"DFS order:{dfs_color(edges2)}")

    print("="*40)

    # edges1 = [(0, 1), (1, 2), (0, 2)]
    # edges2= [(0, 1), (1, 2), (2, 3), (1, 4), (4, 5), (3, 5), (5,6), (6,11), (5,7), (5,8), (5,9)]
    # n2 = len(edges2)

    # print(f"(DFS RECURSION) Connected Graph: {edges2}")
    # print("Adjacency list:")
    # print_adjlist(n2, edges2)
    # print(f"DFS RECURSION order:{rec_dfs(edges2)}")

    # print("="*40)
