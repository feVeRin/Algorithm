# https://www.acmicpc.net/problem/10828

import sys


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def empty(self):
        if not self.size:
            return 1
        return 0

    def push(self, data):
        cur = self.top
        self.top = Node(data)
        self.top.next = cur
        self.size += 1

    def pop(self):
        if not self.empty():
            pop = self.top.val
            self.top = self.top.next
            self.size -= 1
            return pop
        return -1

    def print_top(self):
        if not self.empty():
            return self.top.val
        return -1


if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    s = Stack()

    for i in range(n):
        strs = input().split()
        if strs[0] == 'push':
            s.push(strs[1])
        elif strs[0] == 'pop':
            print(s.pop())
        elif strs[0] == 'size':
            print(s.size)
        elif strs[0] == 'empty':
            print(s.empty())
        elif strs[0] == 'top':
            print(s.print_top())
