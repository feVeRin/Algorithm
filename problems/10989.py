# https://www.acmicpc.net/problem/10989

import sys
import collections

input = sys.stdin.readline

count = collections.defaultdict(int)

n = int(input())
for _ in range(n):
    num = int(input())

    if num in count:
        count[num] += 1
    else:
        count[num] = 1

for item in sorted(count.items()):
    for _ in range(item[1]):
        print(item[0])
