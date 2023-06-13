import sys
input = sys.stdin.readline

n = int(input())
values = sorted(list(map(int, input().split())))
x = int(input())

result = 0
left = 0
right = n-1

while left < right:
    check = values[left] + values[right]

    if check < x:
        left += 1
    elif check > x:
        right -= 1
    else:
        result += 1
        left += 1

print(result)