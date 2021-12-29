for i in range(int(input())):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    dp = []
    idx = 0
    for _ in range(n):
        dp.append(arr[idx:idx+m])
        idx += m

    for j in range(1, m):
        for k in range(n):
            if k == 0:
                leftu = 0
            else:
                leftu = dp[k-1][j-1]
            if k == n-1:
                leftd = 0
            else:
                leftd = dp[k+1][j-1]

            left = dp[k][j-1]
            dp[k][j] = dp[k][j] + max(leftu, leftd, left)

    res = 0
    for i in range(n):
        res = max(res, dp[i][m-1])
    print(res)
