import sys

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())

start = int(input())
graph = [[] for _ in range(n+1)]
visit = [False] * (n+1)
dist = [INF] * (n+1)

for _ in range(m):
    a, b, c, = map(int, input().split())
    graph[a].append([b, c])


def get_smallest_node():
    minV = INF
    idx = 0

    for i in range(1, n+1):
        if dist[i] < minV and not visit[i]:
            minV = dist[i]
            idx = i

    return idx


def dijkstra(start):
    dist[start] = 0
    visit[start] = True

    for j in graph[start]:
        dist[j[0]] = j[1]

    for i in range(n-1):
        now = get_smallest_node()
        visit[now] = True

        for j in graph[now]:
            cost = dist[now] + j[1]
            if cost < dist[j[0]]:
                dist[j[0]] = cost


dijkstra(start)

for i in range(1, n+1):
    if dist[i] == INF:
        print('INF')
    else:
        print(dist[i])
