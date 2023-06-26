import sys
from bisect import bisect_left
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

lis = [A[0]]
for a in A:
    if lis[-1] < a:
        lis.append(a)
    else:
        idx = bisect_left(lis, a)
        lis[idx] = a

print(len(lis))