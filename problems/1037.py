import sys
input = sys.stdin.readline

_ = int(input())
divisors = list(map(int, input().split()))
if len(divisors) == 1:
    print(divisors[0]**2)
else:
    print(min(divisors)*max(divisors))