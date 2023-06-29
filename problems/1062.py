import sys
from itertools import combinations
input = sys.stdin.readline
print = sys.stdout.write

words = []
N, K = map(int, input().split())
words = [input().rstrip() for _ in range(N)]

bits = []
for word in words:
    bit = 0
    for w in word:
        bit |= (1 << (ord(w)-ord('a')))
    bits.append(bit)

remember = 0
for w in 'antic':
    remember |= (1 << (ord(w)-ord('a')))

if K < 5:
    print('0')
else:
    alpha = [1 << i for i in range(26) if not (remember & 1 << i)]
    res = 0

    for comb in combinations(alpha, K-5):
        learn = sum(comb) | remember
        count = 0

        for b in bits:
            if b & learn == b:
                count += 1
        res = max(res, count)
    print(str(res))
