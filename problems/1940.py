import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
steel = sorted(list(map(int, input().split())))
count = 0

start = 0
end = N-1

while start < end:
    if steel[start]+steel[end] > M:
        end -= 1
    elif steel[start]+steel[end] < M:
        start += 1
    else:
        count += 1
        start += 1
        end -= 1

print(count)