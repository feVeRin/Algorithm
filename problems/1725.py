import sys
input = sys.stdin.readline

N = int(input())
stack = []
histogram = []
res = 0

for _ in range(N):
    histo = int(input())
    histogram.append(histo)

histogram.append(0)
stack = [(0, histogram[0])]

for i in range(1, N+1):
    x = i

    while stack and stack[-1][1] > histogram[i]:
        x, y = stack.pop()
        area = (i - x) * y
        res = max(res, area)

    stack.append((x, histogram[i]))

print(res)
