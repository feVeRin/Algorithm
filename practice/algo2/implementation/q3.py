strs = str(input())


def solution(strs):
    res = len(strs)
    for i in range(1, len(strs) // 2 + 1):
        prev = strs[0:i]
        comp = ''
        count = 1
        for j in range(i, len(strs), i):
            if prev == strs[j:j + i]:
                count += 1
            else:
                comp += str(count) + prev if count >= 2 else prev
                prev = strs[j:j + i]
                count = 1

        comp += str(count) + prev if count >= 2 else prev

        res = min(res, len(comp))

    return res


print(solution(strs))
