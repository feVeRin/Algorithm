def binary_search(arr, s, e):
    if s>e:
        return None

    mid = (s+e) // 2

    if arr[mid] == mid:
        return mid
    elif arr[mid] > mid:
        return binary_search(arr, s, mid-1)
    else:
        return binary_search(arr, mid+1, e)


n = int(input())
arr = list(map(int, input().split()))

idx = binary_search(arr, 0, n-1)

if idx is None:
    print(-1)
else:
    print(idx)
