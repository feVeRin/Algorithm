import sys
input = sys.stdin.readline
print = sys.stdout.write

def star(n):
    if n == 1:
        return ['*']

    row = star(n//3) 
    stars = []  
    
    for r in row:
        stars.append(r*3)
    for r in row:
        stars.append(r + ' '*(n//3) + r)
    for r in row:
        stars.append(r * 3)
    return stars

N = int(input())
print('\n'.join(star(N)))
