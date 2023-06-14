import sys
from decimal import *
input = sys.stdin.readline

N = int(input())
for i in range(N):
    tmp = []
    A, B, C, D = map(int, input().split())

    for j in range(-1000000, 1000001):
        if A*j*j*j + B*j*j + C*j + D == 0:
            tmp.append(j)
            break
    
    B += A*tmp[0]
    C += B*tmp[0]
    BAC = B*B-Decimal(4)*A*C
    
    if BAC < 0:
        print(tmp[0])
    elif BAC == 0:
        tmp.append(Decimal(-B/(Decimal(2)*A)))
        tmp.sort()
        if tmp[0] == tmp[1]:
            print(tmp[0])
        else:
            print(tmp[0], tmp[1])
    else:
        tmp.append(Decimal(-B + (B * B - Decimal(4) * A * C) ** Decimal(0.5)) / (Decimal(2) * A))
        tmp.append(Decimal(-B - (B * B - Decimal(4) * A * C) ** Decimal(0.5)) / (Decimal(2) * A))
        tmp.sort()
        if tmp[0] == tmp[1]:
            print(tmp[0], tmp[2])
        elif tmp[1] == tmp[2]:
            print(tmp[0], tmp[1])
        else:
            print(tmp[0], tmp[1], tmp[2])