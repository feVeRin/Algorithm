# https://www.acmicpc.net/problem/2747

import collections
import sys


tb = collections.defaultdict(int)


def fibo(N):
    tb[1] = 1
    for i in range(2, N+1):
        tb[i] = tb[i-1] + tb[i-2]

    return tb[N]


n = int(sys.stdin.readline())
print(fibo(n))
