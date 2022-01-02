# https://www.acmicpc.net/problem/1864

import sys

input = sys.stdin.readline

octa = {'-': 0, '\\': 1, '(': 2, '@': 3, '?': 4, '>': 5, '&': 6, '%': 7, '/': -1}

while True:
    strs = str(input().rstrip())

    if strs == '#':
        break

    res = 0
    for idx, s in enumerate(strs[::-1]):
        res += octa[s] * (8 ** idx)

    print(res)
