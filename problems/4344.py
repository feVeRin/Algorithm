import sys
from decimal import Decimal, ROUND_HALF_UP

def round_half_up(x, decimals):
    precision = "1." + "0" * decimals
    round_x = float(Decimal(str(x)).quantize(Decimal(precision), ROUND_HALF_UP))
    return round_x

input = sys.stdin.readline
c = int(input())
score_list = []

for i in range(c):
    score = list(map(int, input().split()))
    score_list.append(score)

for sc in score_list:
    avg = sum(sc[1:])/sc[0]
    count = 0

    for s in sc[1:]:
        if s > avg:
            count += 1

    print(f'{round_half_up(count/sc[0]*100, 3):.3f}%')
