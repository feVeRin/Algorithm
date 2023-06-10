import sys
input = sys.stdin.readline

def binary_search(left, right):
    while left <= right:
        mid = left + (right - left) // 2
        idx = 0

        for i in range(1, N+1):
            idx += min(mid//i, N)

        if idx < K:
            left = mid + 1
        else:
            tmp = mid
            right = mid - 1
            
    return tmp

if __name__ == '__main__':
    N = int(input())
    K = int(input())

    left = 1
    right = N*N
    result = binary_search(left, right)
    
    print(result)