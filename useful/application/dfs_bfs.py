# https://www.acmicpc.net/problem/1260

import collections

n, m, v = map(int, input().split())

graph = collections.defaultdict(list)

for i in range(m):
    N, M = map(int, input().split())
    graph[N].append(M)
    graph[M].append(N)


def dfs(current, route):
    route.append(current)

    for node in sorted(graph[current]):
        if node not in route:
            route = dfs(node, route)

    return route


def bfs(current):
    route = [current]
    q = collections.deque([current])

    while q:
        pop = q.popleft()
        for node in sorted(graph[pop]):
            if node not in route:
                route.append(node)
                q.append(node)

    return route


print(dfs(v, []))
print(bfs(v))
