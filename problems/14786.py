import sys
import math

input = sys.stdin.readline

if __name__ == '__main__':
    A, B, C = map(int, input().split())

    left = 0
    right = 2*C

    while right-left > 1e-9:
        mid = left + (right - left) / 2
        calc = A*mid + B*math.sin(mid) - C
        
        if calc <= 0:
            left = mid
        else:
            right = mid

    print('%0.19f' %(left + (right - left) / 2))