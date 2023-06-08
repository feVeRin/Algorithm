import sys
input = sys.stdin.readline
N, M = map(int, input().split())

matrix = []
for _ in range(N):
    matrix.append(list(input()))

minimum = min(N, M)
result = 1
for i in range(N):
    for j in range(M):
        for k in range(minimum):
            if ((i + k) < N) and ((j + k) < M) and (matrix[i][j] == matrix[i][j + k] == matrix[i + k][j] == matrix[i + k][j + k]):
                result = max(result, (k + 1))
                
print(result**2)