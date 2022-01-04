# https://www.acmicpc.net/problem/2812

n, k = map(int, input().split())
num = list(input())

stack = []
tmp = k

for i in range(n):
    while stack and tmp > 0:
        if stack[-1] < num[i]:
            stack.pop()
            tmp -= 1
        else:
            break
    stack.append(num[i])

print(''.join(stack[:n-k]))
