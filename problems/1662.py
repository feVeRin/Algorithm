# https://www.acmicpc.net/problem/1662


import sys

input = sys.stdin.readline
strs = str(input().rstrip())
stack = []

for i in range(len(strs)):
    if strs[i] == ')':
        count = 0
        while stack:
            pop = stack.pop()
            if pop == '(':
                break
            else:
                if pop >= 10:
                    count += pop-10
                else:
                    count += 1
        count = count * stack.pop() + 10
        stack.append(count)
    else:
        if strs[i] == '(':
            stack.append(strs[i])
        else:
            stack.append(int(strs[i]))

res = 0
for s in stack:
    if s >= 10:
        res += s-10
    else:
        res += 1

print(res)
