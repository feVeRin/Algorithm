# https://www.acmicpc.net/problem/1081

import sys

input = sys.stdin.readline


def calc(n):
    digit = 1
    dp = [0 for _ in range(10)]
    res = 0

    if n == 0:
        return 0

    while n > 0:
        a = n // (digit*10)
        b = n % (digit*10)

        for i in range(0, 10):
            dp[i] += a*digit

        for i in range(1, b//digit+1):
            dp[i] += digit

        dp[(b//digit+1) % 10] += b % digit
        n -= 9*digit
        digit *= 10

    for i in range(1, 10):
        res += i*dp[i]

    return res


n, m = map(int, input().split())
print(calc(m)-calc(n-1))
