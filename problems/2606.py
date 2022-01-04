# https://www.acmicpc.net/problem/2606

import sys
import collections


input = sys.stdin.readline
n = int(input())
m = int(input())
graph = collections.defaultdict(list)

for _ in range(m):
    N, M = map(int, input().split())
    graph[N].append(M)
    graph[M].append(N)


def bfs(current):
    route = [current]
    q = collections.deque([current])

    while q:
        pop = q.popleft()
        for node in graph[pop]:
            if node not in route:
                route.append(node)
                q.append(node)

    return route[1:]


print(len(bfs(1)))
