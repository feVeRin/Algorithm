n = int(input())

move = input().split()


nx, ny = 0, 0
x, y = 1, 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
walk = ['L', 'R', 'U', 'D']


for m in move:
    for i in range(len(walk)):
        if m == walk[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue

    x, y = nx, ny

print(x, y)
