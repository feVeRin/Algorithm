# https://www.acmicpc.net/problem/1076

import sys

input = sys.stdin.readline

resist = {'black': ('0', 1), 'brown': ('1', 10), 'red': ('2', 100), 'orange': ('3', 1000),
          'yellow': ('4', 10000), 'green': ('5', 100000), 'blue': ('6', 1000000),
          'violet': ('7', 10000000), 'grey': ('8', 100000000), 'white': ('9', 1000000000)}
val = ''

for i in range(3):
    color = input().strip()

    if i != 2:
        val += resist[color][0]
    else:
        val = int(val) * resist[color][1]

print(val)
