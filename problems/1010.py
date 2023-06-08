import sys

input = sys.stdin.readline

def nCr(n, r):
    if r==n:
        return 1
    elif r==1:
        return n
    else:
        return nCr(n, r-1) * (n-r+1) // r

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(nCr(M,N))