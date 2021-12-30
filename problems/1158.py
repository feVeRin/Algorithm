# https://www.acmicpc.net/problem/1158

import sys

input = sys.stdin.readline

n, k = map(int, input().split())
Q = [i for i in range(1, n+1)]
R = []
K = 0

while Q:
    K = (K + (k-1)) % len(Q)
    R.append(str(Q.pop(K)))

res = ', '.join(R)
print('<', res, '>', sep='')
