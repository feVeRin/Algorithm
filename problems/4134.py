import sys
import math
input = sys.stdin.readline

def prime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

T = int(input())
for _ in range(T):
    N = int(input())
    while True:
        if N in [0, 1]:
            print(2)
            break
        if prime(N):
            print(N)
            break
        else:
            N += 1
