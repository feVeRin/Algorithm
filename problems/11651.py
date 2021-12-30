# https://www.acmicpc.net/problem/11651

import sys

input = sys.stdin.readline

n = int(input())
xys = [list(map(int, input().split())) for _ in range(n)]

for xy in sorted(xys, key=lambda x: (x[1], x[0])):
    print(xy[0], xy[1])
