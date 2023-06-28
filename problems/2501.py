import sys
input = sys.stdin.readline

res = set()
N, K = map(int, input().split())
for i in range(1, N//2+1):
    if N % i == 0:
        res.add(i)
        res.add(N//i)

try:
    print(sorted(res)[K-1])
except:
    print(0)