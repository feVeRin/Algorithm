def balanced_idx(p):
    count = 0
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1

        if count == 0:
            return i


def check(p):
    count = 0
    for i in p:
        if i == '(':
            count += 1
        else:
            if count == 0:
                return False
            count -= 1
    return True


def solution(p):
    answer = ''

    if p == '':
        return answer

    idx = balanced_idx(p)
    u = p[:idx+1]
    v = p[idx+1:]

    if check(u):
        answer = u + solution(v)
    else:
        answer = '('
        answer += solution(p)
        answer += ')'

        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('

        answer += ''.join(u)

    return answer
