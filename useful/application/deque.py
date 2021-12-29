# https://www.acmicpc.net/problem/10866

import sys
import collections


if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    q = collections.deque()

    for i in range(n):
        strs = input().split()
        if strs[0] == 'push_front':
            q.appendleft(strs[1])
        elif strs[0] == 'push_back':
            q.append(strs[1])
        elif strs[0] == 'pop_front':
            if len(q) == 0:
                print(-1)
            else:
                print(q.popleft())
        elif strs[0] == 'pop_back':
            if len(q) == 0:
                print(-1)
            else:
                print(q.pop())
        elif strs[0] == 'size':
            print(len(q))
        elif strs[0] == 'empty':
            if len(q) != 0:
                print(0)
            else:
                print(1)
        elif strs[0] == 'front':
            if len(q) == 0:
                print(-1)
            else:
                print(q[0])
        elif strs[0] == 'back':
            if len(q) == 0:
                print(-1)
            else:
                print(q[len(q)-1])
