import heapq
import sys


input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n+1)]
dist = [INF] * (n+1)

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])


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

for i in range(1, n+1):
    if dist[i] == INF:
        print('INF')
    else:
        print(dist[i])
