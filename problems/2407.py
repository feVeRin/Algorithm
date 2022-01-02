# https://www.acmicpc.net/problem/2407

import sys
import collections


memo = collections.defaultdict(int)


def factorial(N):
    if N <= 1:
        return 1
    if memo[N]:
        return memo[N]
    memo[N] = N * factorial(N-1)
    return N * factorial(N-1)


def combination(N, M):
    return factorial(N) // (factorial(M) * factorial(N-M))


input = sys.stdin.readline
n, m = map(int, input().split())

print(combination(n, m))
