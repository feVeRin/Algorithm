n = int(input())

num = [0] * n
num[0] = 1

i2 = i3 = i5 = 0
next2, next3, next5 = 2, 3, 5

for i in range(1, n):
    num[i] = min(next2, next3, next5)
    if num[i] == next2:
        i2 += 1
        next2 = num[i2] * 2
    if num[i] == next3:
        i3 += 1
        next3 = num[i3] * 3
    if num[i] == next5:
        i5 += 1
        next5 = num[i5] * 5

print(num[n-1])
