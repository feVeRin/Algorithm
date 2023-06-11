import sys
input = sys.stdin.readline

N, S = map(int, input().split())
values = list(map(int, input().split()))

result = sys.maxsize
calc = 0
left = 0
right = 0

while True:
    if calc >= S:
        result = min(result, right-left)
        calc -= values[left]
        left += 1
    elif right == N:
        break
    else:
        calc += values[right]
        right += 1


if result == sys.maxsize:
    print(0)
else:
    print(result)