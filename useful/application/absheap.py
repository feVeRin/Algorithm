# https://www.acmicpc.net/problem/11286

import sys
import heapq


input = sys.stdin.readline
n = int(input())
heap = []

for _ in range(n):
    i = int(input())
    if i == 0:
        try:
            x = heapq.heappop(heap)
            print(x[1])
        except:
            print(0)
    else:
        heapq.heappush(heap, (abs(i), i))
