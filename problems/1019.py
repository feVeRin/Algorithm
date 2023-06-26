import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * 10
pages = 1

while N > 0:
    while N % 10 != 9:
        for i in str(N):
            dp[int(i)] += pages
        N -= 1

    if N < 10:
        for i in range(N + 1):
            dp[i] += pages
    else:
        for i in range(10):
            dp[i] += (N // 10 + 1) * pages

    dp[0] -= pages
    pages *= 10
    N //= 10

for i in range(0, 10):
    print(dp[i], end=' ')