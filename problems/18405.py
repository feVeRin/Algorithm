# https://www.acmicpc.net/problem/18405


import sys
import collections

input = sys.stdin.readline
graph = []
virus = []

n, k = map(int, input().split())

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            virus.append((graph[i][j], 0, i, j))

virus.sort()
Q = collections.deque(virus)
s, x, y = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while Q:
    pv, ps, px, py = Q.popleft()
    if ps == s:
        break

    for i in range(4):
        nx = px+dx[i]
        ny = py+dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = pv
                Q.append((pv, ps+1, nx, ny))

print(graph[x-1][y-1])
