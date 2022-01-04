# https://www.acmicpc.net/problem/2669

import sys

input = sys.stdin.readline
res = 0

square = [[0 for _ in range(101)] for _ in range(101)]

for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            square[i][j] = 1

for s in square:
    res += sum(s)

print(res)
