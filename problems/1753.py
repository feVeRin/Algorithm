# https://www.acmicpc.net/problem/1753


import sys
import heapq


input = sys.stdin.readline
INF = sys.maxsize


def dijkstra(v, k, grap):
    heap = []
    dist = [INF] * v
    dist[k-1] = 0
    heapq.heappush(heap, [0, k-1])

    while heap:
        d, n = heapq.heappop(heap)

        for v, w in grap[n]:
            w += d

            if w < dist[v]:
                dist[v] = w
                heapq.heappush(heap, (w, v))

    return dist


if __name__ == '__main__':
    V, E = map(int, input().split())
    start = int(input())

    graph = [[] for _ in range(V)]

    for i in range(E):
        u, v, w = map(int, input().split())
        graph[u-1].append([v-1, w])

    for d in dijkstra(V, start, graph):
        if d != INF:
            print(d)
        else:
            print('INF')
