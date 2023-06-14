import sys
import string
input = sys.stdin.readline

call = list(map(str, input().rstrip()))
tmp = ''
result = 0
dial = []
for alpha in string.ascii_uppercase:
    tmp += alpha
    if alpha in ['R', 'Y']:
        continue

    if len(tmp) in [3, 4]:
        dial.append(tmp)
        tmp = ''

for c in call:
    for d in dial:
        if c in d:
            result += dial.index(d)+3

print(result)