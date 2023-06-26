import sys
input = sys.stdin.readline

seq1 = input().rstrip()
seq2 = input().rstrip()

seq1 = ' ' + seq1
seq2 = ' ' + seq2
dp = [[0] * len(seq2) for _ in range(len(seq1))]

for i in range(1, len(seq1)):
    for j in range(1, len(seq2)):
        if seq1[i] == seq2[j]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])