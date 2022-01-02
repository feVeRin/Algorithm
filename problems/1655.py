# https://www.acmicpc.net/problem/1655


import sys
import heapq
import bisect

input = sys.stdin.readline

n = int(input())
heap = []


for i in range(n):
    x = int(input())
    if len(heap) == 0:
        heapq.heappush(heap, x)
    else:
        idx = bisect.bisect_left(heap, x)
        heap.insert(idx, x)

    length = len(heap)
    if length % 2 == 0:
        print(min(heap[length//2], heap[length//2-1]))
    else:
        print(heap[length//2])
