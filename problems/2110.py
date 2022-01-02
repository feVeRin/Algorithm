# https://www.acmicpc.net/problem/2110

import sys

input = sys.stdin.readline

n, c = map(int, input().split())

arr = [int(input()) for _ in range(n)]
arr.sort()


start = arr[1] - arr[0]
end = arr[-1] - arr[0]

res = 0

while start <= end:
    mid = (start + end) // 2
    tmp = arr[0]
    count = 1

    for i in range(1, len(arr)):
        if arr[i] >= tmp + mid:
            count += 1
            tmp = arr[i]

    if count >= c:
        start = mid + 1
        res = mid
    else:
        end = mid - 1

print(res)
