from collections import deque


def next_pos(pos, board):
    next = []
    pos = list(pos)
    pos1_x, pos1_y, pos2_x, pos2_y = pos[0][0], pos[0][1], pos[1][0], pos[1][1]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        pos1_nx, pos1_ny, pos2_nx, pos2_ny = pos1_x+dx[i], pos1_y+dy[i], pos2_x+dx[i], pos2_y+dy[i]

        if board[pos1_nx][pos1_ny] == 0 and board[pos2_nx][pos2_ny] == 0:
            next.append({(pos1_nx, pos1_ny), (pos2_nx, pos2_ny)})

    if pos1_x == pos2_x:
        for i in [-1, 1]:
            if board[pos1_x+1][pos1_y] == 0 and board[pos2_x+i][pos2_y] == 0:
                next.append({(pos1_x, pos1_y), (pos1_x+i, pos1_y)})
                next.append({(pos2_x, pos2_y), (pos2_x+i, pos2_y)})

    elif pos1_y == pos2_y:
        for i in [-1, 1]:
            if board[pos1_x][pos1_y+1] == 0 and board[pos2_x][pos2_y+i] == 0:
                next.append({(pos1_x, pos1_y), (pos1_x, pos1_y+i)})
                next.append({(pos2_x, pos2_y), (pos2_x, pos2_y+i)})

    return next


def solution(board):
    n = len(board)
    new_board = [[1] * (n+1) for _ in range(n+2)]
    for i in range(n):
        for j in range(n):
            new_board[i+1][j+1] = board[i][j]

    Q = deque()
    visit = []
    pos = {(1, 1), (1, 2)}
    Q.append((pos, 0))
    visit.append(pos)

    while Q:
        pos, cost = Q.popleft()
        if (n, n) in pos:
            return cost

        for nex in next_pos(pos, new_board):
            if nex not in visit:
                Q.append((nex, cost+1))
                visit.append(nex)

    return 0
