# https://www.acmicpc.net/problem/2108

import sys
import collections

input = sys.stdin.readline

n = int(input())
nums = []
tmp = []

for _ in range(n):
    i = int(input())
    nums.append(i)

nums.sort()
mc = collections.Counter(nums).most_common()

print(int(round(sum(nums)/len(nums), 0)))
print(nums[len(nums)//2])
for m in sorted(mc, key=lambda x: x[1], reverse=True):
    if m[1] == mc[0][1]:
        tmp.append(m[0])
    else:
        break

if len(tmp) == 1:
    print(tmp[0])
else:
    print(tmp[1])

print(max(nums)-min(nums))
