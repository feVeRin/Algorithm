# https://www.acmicpc.net/problem/1924

import sys

input = sys.stdin.readline

count = 0
m, d = map(int, input().split())

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
dow = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

for i in range(m-1):
    count += days[i]

print(dow[(count+d) % 7])
