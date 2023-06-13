import sys
input = sys.stdin.readline

N, M = map(int, input().split())

matrix1 = []
matrix2 = []

for _ in range(N):
    matrix1.append(list(map(int, input().split())))

for _ in range(N):
    matrix2.append(list(map(int, input().split())))

for i in range(N):
    for j in range(M):
        result = matrix1[i][j] + matrix2[i][j]
        print(result, end=' ')
    print()
