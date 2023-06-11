import sys
input = sys.stdin.readline

N = int(input())

for i in range(1, 2*N+1, 2):
    star = '*'*i
    blank = ' '*(((2*N+1)-i)//2-1)
    result = blank+star
    print(result)

for i in range(2*N-3, 0, -2):
    star = '*'*i
    blank = ' '*(((2*N-3)-i)//2+1)
    result = blank+star
    print(result)