import sys
input = sys.stdin.readline

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]

result = [[0 for _ in range(N)] for _ in range(N)]
count = 0

for i in range(N):
    for j in range(N):
        for k in range(N):
            result[i][j] |= A[i][k] & B[k][j]
        if result[i][j] == 1:
            count+=1

print(count)