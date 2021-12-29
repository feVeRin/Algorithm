import heapq
import sys


INF = sys.maxsize

V, E = map(int, input().split())
start = int(input())

graph = [[] for _ in range(V+1)]
dist = [INF] * (V + 1)

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])


def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0, start))
    dist[start] = 0

    while heap:
        d, node = heapq.heappop(heap)

        for v, w in graph[node]:
            w += d
            if w < dist[v]:
                dist[v] = w
                heapq.heappush(heap, (w, v))


dijkstra(start)
for d in dist:
    if d == INF:
        print('INF')
    else:
        print(d)
