# https://www.acmicpc.net/problem/1715


import sys
import heapq


input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    card = int(input())
    heapq.heappush(heap, card)

count = 0

while len(heap) != 1:
    c1 = heapq.heappop(heap)
    c2 = heapq.heappop(heap)
    sum_c = c1+c2
    count += sum_c

    heapq.heappush(heap, sum_c)

print(count)
