import sys
import math
input = sys.stdin.readline

def test(X, Y, x, y, N):
    tmp = 0
    for i in range(N):
        grad = (X[i]-x) * (X[i]-x) + (Y[i]-y) * (Y[i]-y)
        tmp  += math.sqrt(grad)
    return tmp

if __name__ == '__main__':
    X, Y = [], []
    N = int(input())
    for _ in range(N):
        _x, _y = map(int, input().split())
        X.append(_x)
        Y.append(_y)
    
    x = 0
    y = 10000
    delta = 500

    while delta > 0.0001:
        if test(X, Y, x, y+delta, N) < test(X, Y, x, y, N):
            y += delta
        if test(X, Y, x, y-delta, N) < test(X, Y, x, y, N):
            y -= delta
        if test(X, Y, x+delta, y, N) < test(X, Y, x, y, N):
            x += delta
        if test(X, Y, x-delta, y, N) < test(X, Y, x, y, N):
            x -= delta
        
        delta *= 0.9

    print("%0.0lf" %test(X, Y, x, y, N))