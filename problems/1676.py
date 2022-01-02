# https://www.acmicpc.net/problem/1676

import sys
import collections

memo = collections.defaultdict(int)
input = sys.stdin.readline


def factorial(N):
    if N <= 1:
        return 1
    if memo[N]:
        return memo[N]

    memo[N] = N * factorial(N-1)

    return memo[N]


if __name__ == '__main__':
    count = 0
    n = int(input())
    res = factorial(n)

    for r in str(res)[::-1]:
        if r != '0':
            break
        count += 1

    print(count)
