import sys
input = sys.stdin.readline

while True:
    triangle = list(map(int, input().split()))
    if triangle == [0,0,0]:
        break
    
    triangle = sorted(triangle)
    if triangle[0] + triangle[1] <= triangle[2]:
        print('Invalid')
    else:
        if triangle[0] == triangle[1] == triangle[2]:
            print('Equilateral')
        elif (triangle[0] == triangle[1]) or (triangle[1] == triangle[2]) or (triangle[0] == triangle[2]):
            print('Isosceles')
        else:
            print('Scalene')