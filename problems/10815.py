import sys
from collections import Counter
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())
    cards = list(map(int, input().split()))
    M = int(input())
    values = list(map(int, input().split()))

    counter = Counter(cards)

    for v in values:
        if v in counter:
            print('1', end=' ')
        else:
            print('0', end=' ')
