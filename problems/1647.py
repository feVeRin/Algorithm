# https://www.acmicpc.net/problem/1647


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


v, e = map(int, input().split())
parent = [0] * (v+1)

for i in range(1, v+1):
    parent[i] = i

edges = []
result = 0
tmp = 0

for i in range(e):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

for edge in sorted(edges):
    cost, a, b = edge
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        result += cost
        tmp = cost

print(result - tmp)
