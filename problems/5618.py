# https://www.acmicpc.net/problem/5618

import sys

input = sys.stdin.readline

n = int(input())


def GCD(x, y):
    if x == 0:
        return y

    return GCD(y % x, x)


nums = list(map(int, input().split()))

gcd = GCD(nums[0], GCD(nums[1], nums[-1]))
for i in range(1, gcd//2 + 1):
    if gcd % i == 0:
        print(i)
print(gcd)
