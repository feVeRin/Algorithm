# https://www.acmicpc.net/problem/2581


import sys
import math

input = sys.stdin.readline


def prime(num):
    if num == 1:
        return

    n = int(math.sqrt(num))
    for k in range(2, n+1):
        if num % k == 0:
            return

    return num


N = int(input())
M = int(input())
res = []

for i in range(N, M+1):
    p = prime(i)
    if p:
        res.append(p)


if res:
    print(sum(res))
    print(res[0])
else:
    print(-1)
