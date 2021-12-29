n, m = map(int, input().split())

d = [[0]*m for _ in range(n)]

x, y, direction = map(int, input().split())
d[x][y] = 1

world = []
for _ in range(n):
    world.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def turning():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


count = 1
turn = 0

while True:
    turning()
    nx = x + dx[direction]
    ny = y + dy[direction]

    if d[nx][ny] == 0 and world[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn = 0
        continue

    else:
        turn += 1

    if turn == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        if world[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn = 0

print(count)
