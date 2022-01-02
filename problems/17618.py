# https://www.acmicpc.net/problem/17618

import sys

input = sys.stdin.readline

count = 0
n = int(input())
dp = [0 for _ in range(n+1)]

for i in range(1, n+1):
    dp[i] = dp[i // 10] + (i % 10)

    if i % dp[i] == 0:
        count += 1

print(count)
