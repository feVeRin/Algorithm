# https://www.acmicpc.net/problem/10610

import sys

input = sys.stdin.readline

N = sorted(list(input().strip()), reverse=True)

number = ''.join(N)
if int(number) % 30 != 0:
    print(-1)
else:
    print(number)
