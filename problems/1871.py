# https://www.acmicpc.net/problem/1871

import sys

input = sys.stdin.readline


n = int(input())
for _ in range(n):
    front, back = map(str, input().rstrip().split('-'))
    res1 = 0
    res2 = int(back)

    for idx, f in enumerate(front[::-1]):
        num = ord(f)-ord('A')
        res1 += num * 26**idx

    if abs(res1-res2) < 101:
        print('nice')
    else:
        print('not nice')
