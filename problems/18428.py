# https://www.acmicpc.net/problem/18428

import sys
import itertools


input = sys.stdin.readline

n = int(input())
board = []
teachers = []
spaces = []

for i in range(n):
    board.append(list(input().split()))

    for j in range(n):
        if board[i][j] == 'T':
            teachers.append((i, j))

        if board[i][j] == 'X':
            spaces.append((i, j))


def find(x, y, direction):
    if direction == 0:
        while y >= 0:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            y -= 1

    if direction == 1:
        while y < n:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            y += 1

    if direction == 2:
        while x >= 0:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            x -= 1

    if direction == 3:
        while x < n:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            x += 1

    return False


def solution():
    for x, y in teachers:
        for i in range(4):
            if find(x, y, i):
                return True

    return False


flag = False

for combi in itertools.combinations(spaces, 3):
    for x, y in combi:
        board[x][y] = 'O'

    if not solution():
        flag = True
        break

    for x, y in combi:
        board[x][y] = 'X'


if flag:
    print('YES')
else:
    print('NO')
