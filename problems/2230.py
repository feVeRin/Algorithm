import sys
input = sys.stdin.readline

N, M = map(int, input().split())
seqA = []
for _ in range(N):
    seqA.append(int(input()))

seqA.sort()
result = sys.maxsize
left = 0
right = 0

while left <= right and right < N:
    check = seqA[right] - seqA[left]

    if check < M:
        right += 1
    else:
        result = min(result, check)
        left += 1

print(result)