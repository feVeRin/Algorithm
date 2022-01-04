# https://www.acmicpc.net/problem/2960

import sys

input = sys.stdin.readline

N, K = map(int, input().split())
nums = list(range(2, N+1))


def find(num, k):
    count = 0

    while num:
        p = num[0]
        tmp = 0

        while tmp < len(num):
            if num[tmp] % p == 0:
                count += 1
                if count == K:
                    return num[tmp]

                num.pop(tmp)
                tmp -= 1
            tmp += 1


print(find(nums, K))
