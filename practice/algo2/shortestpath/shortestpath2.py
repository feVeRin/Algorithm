import heapq

INF = int(1e9)

n, m , start = map(int, input().split())

graph = [[] for _ in range(n+1)]
dist = [INF] * (n+1)

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append([y, z])


def dijkstra(start):
    Q = []
    heapq.heappush(Q, (0, start))
    dist[start] = 0

    while Q:
        di, node = heapq.heappop(Q)

        if dist[node] < di:
            continue

        for i in graph[node]:
            cost = di + i[1]
            if cost < dist[i[0]]:
                dist[i[0]] = cost
                heapq.heappush(Q, (cost, i[0]))


dijkstra(start)
count = 0
max_dist = 0

for d in dist:
    if d != INF:
        count += 1
        max_dist = max(max_dist, d)

print(count-1, max_dist)
