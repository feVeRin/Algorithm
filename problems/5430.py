import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for t in range(T):
    ps = input()
    n = int(input())
    nums = input().strip()
    deQ = deque(nums[1:-1].split(','))
    
    flag = False
    rev = 0

    if n == 0:
        deQ = deque()

    for i in range(len(ps)):
        if ps[i] == 'R':
            rev += 1
        elif ps[i] == 'D':
            if len(deQ) == 0:
                flag = True
                break
            else:
                if rev % 2 == 0:
                    deQ.popleft()
                else:
                    deQ.pop()
    
    if flag:
        print('error')
    else:
        if rev % 2 == 0:
            print('['+",".join(deQ)+']')
        else:
            deQ.reverse()
            print('['+",".join(deQ)+']')