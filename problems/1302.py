# https://www.acmicpc.net/problem/1302


import sys
import collections


input = sys.stdin.readline

N = int(input())
books = [str(input().rstrip()) for _ in range(N)]
counter = collections.Counter(books).most_common()

max_c = counter[0][1]
res = []

for c in counter:
    if c[1] == max_c:
        res.append(c[0])
    else:
        break

print(sorted(res)[0])
