# https://www.acmicpc.net/problem/14719

import sys

input = sys.stdin.readline

h, w = map(int, input().split())
blocks = list(map(int, input().split()))
count = 0
stack = []

for i in range(len(blocks)):
    while stack and (blocks[i] > blocks[stack[-1]]):
        pop = stack.pop()

        if not len(stack):
            break

        dist = i - stack[-1] - 1
        water = min(blocks[i], blocks[stack[-1]]) - blocks[pop]

        count += dist * water

    stack.append(i)

print(count)
