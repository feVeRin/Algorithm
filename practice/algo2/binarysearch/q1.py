from bisect import bisect_left, bisect_right


def count_v(arr, left, right):
    r = bisect_right(arr, right)
    l = bisect_left(arr, left)
    return r-l


n, x = map(int, input().split())
arr = list(map(int, input().split()))

count = count_v(arr, x, x)

if count == 0:
    print(-1)
else:
    print(count)
