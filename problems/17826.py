# https://www.acmicpc.net/problem/17826

import sys

input = sys.stdin.readline

scores = list(map(int, input().split()))
my = int(input())

if my in scores[:5]:
    print('A+')
elif my in scores[5:15]:
    print('A0')
elif my in scores[15:30]:
    print('B+')
elif my in scores[30:35]:
    print('B0')
elif my in scores[35:45]:
    print('C+')
elif my in scores[45:48]:
    print('C0')
else:
    print('F')
