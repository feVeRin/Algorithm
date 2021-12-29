N = int(input())

nums = list(map(int, input().split()))

nums.sort()
res = 1

for n in nums:
    if res < n:
        break
    res += n

print(res)
