import sys

input = sys.stdin.readline

n, m = map(int,input().split())
x, y, d = map(int,input().split())

array = []
for _ in range(n):
    array.append(list(map(int,input().split())))

visited = [[0] * m for _ in range(n)]
visited[x][y] = 1

dx = [-1, 0, 1, 0]  
dy = [0, 1, 0, -1]

def turn_left():
    global d

    d -= 1
    if d == -1:
        d = 3

turn_time = 0
count = 1

while True:
    turn_left()
    nx = x + dx[d]
    ny = y + dy[d]
    
    if array[nx][ny] == 0 and visited[nx][ny] == 0:
        x = nx
        y = ny
        visited[nx][ny] = 1
        turn_time = 0
        count += 1
    else:
        turn_time += 1
    if turn_time == 4:
        nx = x - dx[d]
        ny = y - dy[d]
        if array[nx][ny] == 0:
            x = nx
            y = ny
            turn_time = 0
        else:
            break

print(count)