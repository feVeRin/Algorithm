# https://www.acmicpc.net/problem/1920

import sys

input = sys.stdin.readline


def binary_search(num_list, x, left, right):
    try:
        if left <= right:
            mid = left + (right - left) // 2

            if num_list[mid] < x:
                return binary_search(num_list, x, mid + 1, right)
            elif num_list[mid] > x:
                return binary_search(num_list, x, left, mid - 1)
            else:
                return mid
    except:
        return None


if __name__ == '__main__':
    N = int(input())
    num = list(map(int, input().split()))
    num.sort()

    M = int(input())
    find = list(map(int, input().split()))

    for f in find:
        idx = binary_search(num, f, 0, len(num))
        if idx is not None:
            print(1)
        else:
            print(0)
