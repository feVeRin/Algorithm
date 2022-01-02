# https://www.acmicpc.net/problem/17388

import sys

input = sys.stdin.readline

s, k, h = map(int, input().split())

if s+k+h >= 100:
    print('OK')
else:
    min_skh = min(s, k, h)

    if min_skh == s:
        print('Soongsil')
    elif min_skh == k:
        print('Korea')
    else:
        print('Hanyang')
