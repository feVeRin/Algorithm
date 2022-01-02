# https://www.acmicpc.net/problem/18352


import sys
import collections


input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

dist = [-1] * (n+1)
dist[x] = 0
Q = collections.deque([x])

while Q:
    pop = Q.popleft()
    for node in graph[pop]:
        if dist[node] == -1:
            dist[node] = dist[pop] + 1
            Q.append(node)

check = False
for i in range(1, n+1):
    if dist[i] == k:
        print(i)
        check = True

if not check:
    print(-1)
