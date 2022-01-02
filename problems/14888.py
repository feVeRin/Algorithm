# https://www.acmicpc.net/problem/14888

import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int,  input().split()))
add, sub, mul, div = map(int, input().split())

min_n = sys.maxsize
max_n = -sys.maxsize


def solution(i, num):
    global min_n, max_n, add, sub, mul, div

    if i == n:
        min_n = min(min_n, num)
        max_n = max(max_n, num)

    else:
        if add > 0:
            add -= 1
            solution(i+1, num+nums[i])
            add += 1

        if sub > 0:
            sub -= 1
            solution(i+1, num-nums[i])
            sub += 1

        if mul > 0:
            mul -= 1
            solution(i+1, num*nums[i])
            mul += 1

        if div > 0:
            div -= 1
            solution(i+1, int(num/nums[i]))
            div += 1


solution(1, nums[0])
print(max_n)
print(min_n)
