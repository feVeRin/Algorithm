# https://www.acmicpc.net/problem/1918

import sys

input = sys.stdin.readline


def to_postfix(expression):
    stack = []
    postfix = ''
    priority = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2}

    for exp in expression:
        if exp.isalpha():
            postfix += exp
        else:
            if exp == '(':
                stack.append(exp)
            elif exp == ')':
                pop = stack.pop()
                while pop != '(':
                    postfix += pop
                    pop = stack.pop()
            else:
                while stack and priority[exp] <= priority[stack[-1]]:
                    postfix += stack.pop()
                stack.append(exp)

    while stack:
        postfix += stack.pop()

    return postfix


infix = str(input().rstrip())
print(to_postfix(infix))
