xy = input()

x = int(xy[1])
y = int(ord(xy[0])-int(ord('a'))+1)

step = [(2,1), (2,-1), (-2,1), (-2,-1), (1,2), (1,-2), (-1,2), (-1,2)]

count = 0

for s in step:
    nx = x + s[0]
    ny = y + s[1]

    if 1 <= nx <= 8 and 1 <= ny <= 8:
        count += 1

print(count)
