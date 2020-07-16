import collections
from typing import List


def criticalConnections(n, connections):

    graph = collections.defaultdict(list)
    for conn in connections:
        graph[conn[0]].append(conn[1])
        graph[conn[1]].append(conn[0])

    connections = set(map(tuple, (map(sorted, connections))))
    rank = {i: None for i in range(n)}

    print(dict(graph))
    print(connections)
    print(rank)

    def dfs(node, depth):
        if rank[node]:
            return rank[node]

        rank[node] = depth
        min_back_depth = n

        for neighbor in graph[node]:
            if rank[neighbor] == depth - 1:
                continue
            back_depth = dfs(neighbor, depth + 1)
            if back_depth <= depth:
                connections.discard(tuple(sorted((node, neighbor))))
            min_back_depth = min(min_back_depth, back_depth)
        return min_back_depth

    dfs(0, 0)

    return list(connections)

print(criticalConnections(4,[[0,1],[1,2],[2,0],[1,3]]))