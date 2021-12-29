import heapq

INF = int(1e9)

n, m = map(int, input().split())
start = 1
graph = [[] for i in range(n+1)]
dist = [INF] * (n+1)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append([v, 1])
    graph[v].append([u, 1])


def dijkstra(start):
    Q = []
    heapq.heappush(Q, (0, start))
    dist[start] = 0

    while Q:
        di, node = heapq.heappop(Q)

        if dist[node] < di:
            continue

        for g in graph[node]:
            cost = di + g[1]

            if cost < dist[g[0]]:
                dist[g[0]] = cost
                heapq.heappush(Q, (cost, g[0]))


dijkstra(start)
max_n = 0
max_d = 0
res = []

for i in range(1, n+1):
    if max_d < dist[i]:
        max_n = i
        max_d = dist[i]
        res = [max_n]
    elif max_d == dist[i]:
        res.append(i)

print(max_n, max_d, len(res))
