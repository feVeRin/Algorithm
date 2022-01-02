# https://www.acmicpc.net/problem/1916

import sys
import collections
import heapq


input = sys.stdin.readline
n = int(input())
m = int(input())

graph = collections.defaultdict(list)

for i in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

start, end = map(int, input().split())

heap = []
heapq.heappush(heap, [0, start])

while heap:
    price, n = heapq.heappop(heap)

    if n == end:
        print(price)

    for v, w in graph[n]:
        tmp = price + w
        heapq.heappush(heap, (v, tmp))
