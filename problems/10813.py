import sys
input = sys.stdin.readline

N, M = map(int, input().split())

basket = list(range(1, N+1))

for _ in range(M):
    i, j = map(int, input().split())
    tmp = basket[i-1]
    basket[i-1] = basket[j-1]
    basket[j-1] = tmp

for b in basket:
    print(b, end=' ')