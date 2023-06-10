import sys
from decimal import *

getcontext().prec = 60
getcontext().rounding = ROUND_HALF_UP
input = sys.stdin.readline
pi = Decimal('3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067982148086513282306647093844609550582231725359408128481117450284102701938521105559644622948954930381964428810')

def sin(x):
    if -pi <= x <= pi:
        getcontext().prec += 2
        i, lasts, s, fact, num, sign = 1, 0, x, 1, x, 1
        while s != lasts:
            lasts = s
            i += 2
            fact *= i * (i-1)
            num *= x * x
            sign *= -1
            s += num / fact * sign
        getcontext().prec -= 2
        return +s
    elif x > pi:
        while x > pi:
            x-=2*pi
        return sin(x)
    elif x < -pi:
        while x < -pi:
            x+=2*pi
        return sin(x)

def F(a,b,c,x):
    return a*x + b*Decimal(sin(x)) - c

if __name__ == '__main__':
    A, B, C = map(Decimal, map(int, input().split()))

    left = C/A - Decimal('1')
    right = C/A + Decimal('1')

    while right-left > Decimal('1e-30'):
        mid = left + (right - left) / 2
        
        if F(A,B,C,mid) > 0:
            right = mid
        elif F(A,B,C,mid) < 0:
            left = mid
        else:
            break

    print(round(left + (right - left) / 2, 6))
