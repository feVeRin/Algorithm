# https://www.acmicpc.net/problem/16234

import sys
import collections

input = sys.stdin.readline

n, l, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
res = 0


def bfs(x, y, idx):
    info = [(x, y)]
    Q = collections.deque()
    Q.append((x, y))

    union[x][y] = idx
    population = graph[x][y]
    count = 1

    while Q:
        x, y = Q.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                    Q.append((nx, ny))
                    union[nx][ny] = idx
                    population += graph[nx][ny]
                    count += 1
                    info.append((nx, ny))

    for i, j in info:
        graph[i][j] = population // count

    return count


total = 0
while True:
    union = [[-1]*n for _ in range(n)]
    idx = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:
                bfs(i, j, idx)
                idx += 1

    if idx == n*n:
        break

    total += 1

print(total)
