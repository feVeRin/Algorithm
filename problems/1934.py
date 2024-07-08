import sys

input = sys.stdin.readline


def gcd(x,y):
    if y==0:
        return x
    else:
        return gcd(y, x%y)

def lcm(x,y):
    return (x*y)//gcd(x,y)

t = int(input())
for _ in range(t):
    a,b = map(int, input().split())
    print(lcm(a,b))
