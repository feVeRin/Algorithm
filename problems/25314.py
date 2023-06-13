import sys
input = sys.stdin.readline

N = int(input().rstrip())
result = ''

for i in range(N//4):
    result += 'long '

print(result+'int')