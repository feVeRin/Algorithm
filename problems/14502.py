# https://www.acmicpc.net/problem/14502


import sys

input = sys.stdin.readline

n, m = map(int, input().split())
info = []
tmp = [[0] * m for _ in range(n)]

for _ in range(n):
    info.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
res = 0


def virus(x, y):
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if tmp[nx][ny] == 0:
                tmp[nx][ny] = 2
                virus(nx, ny)


def safe_area():
    area = 0
    for i in range(n):
        for j in range(m):
            if tmp[i][j] == 0:
                area += 1

    return area


def dfs(count):
    global res

    if count == 3:
        for i in range(n):
            for j in range(m):
                tmp[i][j] = info[i][j]

        for i in range(n):
            for j in range(m):
                if tmp[i][j] == 2:
                    virus(i, j)

        res = max(res, safe_area())
        return

    for i in range(n):
        for j in range(m):
            if info[i][j] == 0:
                info[i][j] = 1
                count += 1
                dfs(count)
                info[i][j] = 0
                count -= 1


dfs(0)
print(res)
