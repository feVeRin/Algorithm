from bisect import bisect_left, bisect_right


def count(a, left, right):
    r = bisect_right(a, right)
    l = bisect_left(a, left)
    return r-l


arr = [[] for _ in range(10001)]
reverse = [[] for _ in range(10001)]


def solution(words, queries):
    answer = []
    for word in words:
        arr[len(word)].append(word)
        reverse[len(word)].append(word[::-1])

    for i in range(10001):
        arr[i].sort()
        reverse[i].sort()

    for q in queries:
        if q[0] != '?':
            res = count(arr[len(q)], q.replace('?', 'a'), q.replace('?', 'z'))
        else:
            res = count(reverse[len(q)], q[::-1].replace('?', 'a'), q[::-1].replace('?', 'z'))
        answer.append(res)

    return answer
