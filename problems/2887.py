# https://www.acmicpc.net/problem/2887

import sys

input = sys.stdin.readline


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n = int(input())
parent = [0] * (n+1)
edge = []
res = 0

for i in range(1, n+1):
    parent[i] = i

X, Y, Z = [], [], []

for i in range(1, n+1):
    x, y, z = map(int, input().split())
    X.append((x, i))
    Y.append((y, i))
    Z.append((z, i))

X.sort()
Y.sort()
Z.sort()

for i in range(n-1):
    edge.append((X[i + 1][0] - X[i][0], X[i][1], X[i + 1][1]))
    edge.append((Y[i + 1][0] - Y[i][0], Y[i][1], Y[i + 1][1]))
    edge.append((Z[i + 1][0] - Z[i][0], Z[i][1], Z[i + 1][1]))

edge.sort()

for c, a, b in edge:
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        res += c

print(res)
