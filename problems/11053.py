# https://www.acmicpc.net/problem/11053

import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr = [-sys.maxsize] + arr
N = len(arr)
dp = [-1] * N


def lis(n):
    if dp[n] != -1:
        return dp[n]

    res = 0
    for i in range(n + 1, N):
        if arr[n] < arr[i]:
            res = max(res, lis(i) + 1)

    dp[n] = res
    return res


print(lis(0))
