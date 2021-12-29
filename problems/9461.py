# https://www.acmicpc.net/problem/9461

import sys
import collections

input = sys.stdin.readline

T = int(input())

tb = collections.defaultdict(int)


def padovan(n):
    tb[0] = 1
    tb[1] = 1
    tb[2] = 1

    for i in range(2, n+1):
        tb[i] = tb[i-2] + tb[i-3]
    return tb[n-1]


for _ in range(T):
    N = int(input())
    print(padovan(N))