# https://www.acmicpc.net/problem/1316

import sys
import collections


def groupcheck(word):
    check = collections.defaultdict(list)
    for idx, w in enumerate(word):
        if w not in check:
            check[w].append(idx)
        else:
            if idx != (check[w].pop())+1:
                return False
            else:
                check[w].append(idx)

    return True


if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    res = []

    for _ in range(n):
        strs = str(input())
        res.append(groupcheck(strs))

    print(sum(res))
