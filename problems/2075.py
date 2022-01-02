# https://www.acmicpc.net/problem/2075

import heapq
import sys


input = sys.stdin.readline
N = int(input())
heap = []
minn = 0

for i in range(N):
    num = map(int, input().split())
    if i == 0:
        for n in num:
            heapq.heappush(heap, n)
        minn = heap[0]
    else:
        for n in num:
            if n > minn:
                heapq.heappush(heap, n)
                heapq.heappop(heap)
                minn = heap[0]

print(heap[0])
