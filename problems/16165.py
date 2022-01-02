# https://www.acmicpc.net/problem/16165

import sys
import collections


input = sys.stdin.readline

n, m = map(int, input().split())
table = collections.defaultdict(list)

for _ in range(n):
    name = []
    group = input().strip()
    num = int(input())

    for j in range(num):
        name.append(input().strip())

    table[group] = name

for _ in range(m):
    answer = input().strip()
    prob = int(input())

    if prob == 0:
        member = sorted(table[answer])
        print('\n'.join(member))
    else:
        for group, name in table.items():
            if answer in name:
                print(group)
                break
