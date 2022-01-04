# https://www.acmicpc.net/problem/2566

import sys


input = sys.stdin.readline
res, res_row, res_col = 0, 0, 0


for i in range(9):
    row = list(map(int, input().split()))
    tmp = max(row)
    if tmp >= res:
        res = tmp
        res_row = i
        res_col = row.index(res)

print(res)
print(res_row+1, res_col+1)
