# https://www.acmicpc.net/problem/1182

import sys

input = sys.stdin.readline

n, s = map(int, input().split())
nums = list(map(int, input().split()))
count = 0


def solution(idx, sum):
    global count

    if idx >= n:
        return

    sum += nums[idx]
    if sum == s:
        count += 1

    solution(idx + 1, sum - nums[idx])
    solution(idx + 1, sum)


solution(0, 0)
print(count)
