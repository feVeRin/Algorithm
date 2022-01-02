# https://www.acmicpc.net/problem/2166

import sys

input = sys.stdin.readline


def calc(x1, y1, x2, y2, x3, y3):
    return (x1*y2 + x2*y3 + x3*y1) - (y1*x2 + y2*x3 + y3*x1)


n = int(input())
res = 0
x, y = map(int, input().split())
xy = [list(map(int, input().split())) for _ in range(n-1)]

for i in range(n-2):
    res += calc(x, y, xy[i][0], xy[i][1], xy[i+1][0], xy[i+1][1])

print(abs(res)/2)
