# https://www.acmicpc.net/problem/11816

import sys

input = sys.stdin.readline

x = str(input().rstrip())
hexcode = {'a':10, 'b':11, 'c':12, 'd':13, 'e':14, 'f': 15}
res = 0

if x[0] == '0':
    if x[1] == 'x':
        for idx, num in enumerate(x[2:][::-1]):
            if num in hexcode:
                res += hexcode[num] * (16**idx)
            else:
                res += int(num) * (16**idx)
        print(res)
    else:
        for idx, num in enumerate(x[1:][::-1]):
            res += int(num) * (8**idx)
        print(res)
else:
    print(int(x))
