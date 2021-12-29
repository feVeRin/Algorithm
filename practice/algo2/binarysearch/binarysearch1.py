import bisect

N = int(input())

num = list(map(int, input().split()))
num.sort()

M = int(input())
num2 = list(map(int, input().split()))


for i in num2:
    idx = bisect.bisect_left(num, i)

    if idx < len(num) and num[idx] == i:
        print('yes')
    else:
        print('no')
