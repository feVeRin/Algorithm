# https://www.acmicpc.net/problem/3190

import sys

input = sys.stdin.readline

n = int(input())
k = int(input())

direction = []
maps = [[0] * (n+1) for _ in range(n+1)]
for _ in range(k):
    x, y = map(int, input().split())

l = int(input())
for _ in range(l):
    x, c = input().split()
    direction.append((int(x), c))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def rotation(d, c):
    if c == 'L':
        d = (d-1) % 4
    else:
        d = (d+1) % 4

    return d


def snake():
    x, y = 1, 1
    maps[x][y] = 2
    d = 0
    time = 0
    idx = 0

    Q = [(x, y)]

    while True:
        nx = x + dx[d]
        ny = y + dy[d]

        if 1 <= nx <= n and 1 <= ny <= n and maps[nx][ny] != 2:
            if maps[nx][ny] == 0:
                maps[nx][ny] = 2
                Q.append((nx, ny))

                xx, yy = Q.pop(0)
                maps[xx][yy] = 0

            if maps[nx][ny] == 1:
                maps[nx][ny] = 2
                Q.append((nx, ny))

        else:
            time += 1
            break

        x, y = nx, ny
        time += 1

        if idx < 1 and time == direction[idx][0]:
            d = rotation(d, direction[idx][1])
            idx += 1

    return time


print(snake())
