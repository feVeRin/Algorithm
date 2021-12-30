# https://www.acmicpc.net/problem/11055

import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp = [0] * n
res = 0


for i in range(n):
    dp[i] = dp[i]+arr[i]

    for j in range(i):
        if arr[i] > arr[j] and dp[i] < dp[j] + arr[i]:
            dp[i] = dp[j] + arr[i]

    if res < dp[i]:
        res = dp[i]

print(max(dp))
