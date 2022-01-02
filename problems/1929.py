# https://www.acmicpc.net/problem/1929

import sys
import math


input = sys.stdin.readline
N, M = map(int, input().split())


def prime(num):
    if num == 1:
        return

    n = int(math.sqrt(num))
    for k in range(2, n+1):
        if num % k == 0:
            return

    print(num)


for i in range(N, M+1):
    prime(i)
