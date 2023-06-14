import sys
input = sys.stdin.readline

def facto(N):
    dp = [1]*21
    for i in range(1, N+1):
        dp[i] = dp[i-1] * i
    return dp[N]

N = int(input())
print(facto(N))