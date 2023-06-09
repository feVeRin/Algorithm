# https://www.acmicpc.net/problem/1655

import sys
import heapq
input = sys.stdin.readline

n = int(input())
maxheap = []
minheap = []

for i in range(n):
    x = int(input())
    if len(maxheap) == len(minheap):
        heapq.heappush(maxheap, -x)
    else:
        heapq.heappush(minheap, x)
    
    if len(maxheap) >= 1 and len(minheap) >= 1 and maxheap[0] * (-1) > minheap[0]:
        maxpop = heapq.heappop(maxheap) * (-1)
        minpop = heapq.heappop(minheap)

        heapq.heappush(maxheap, minpop * (-1))
        heapq.heappush(minheap, maxpop)

    print(maxheap[0] * (-1))