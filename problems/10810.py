import sys
input = sys.stdin.readline

N, M = map(int, input().split())

basket = [0]*N
for _ in range(M):
    i, j, k = map(int, input().split())
    for t in range(i-1, j):
        basket[t] = k

for b in basket:
    print(b, end=' ')