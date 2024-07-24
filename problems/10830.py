import sys

input = sys.stdin.readline

def multiply(X, Y):
    XY = [[0]*len(Y[0]) for _ in range(len(X))]

    for i in range(len(X)):
        for j in range(len(Y[0])):
            for k in range(len(X[0])):
                XY[i][j] += X[i][k]*Y[k][j] %1000

    return XY

def power(X, n):
    if n == 1:
        return X
    elif n%2 == 0:
        return power(multiply(X,X), n//2)
    else:
        return multiply(X, power(multiply(X,X), (n-1)//2))

matrix = []
n, b = map(int, input().split())
for _ in range(n):
    matrix.append(list(map(int, input().split())))

for row in power(matrix, b):
    print(*[r % 1000 for r in row])