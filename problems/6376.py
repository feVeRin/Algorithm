# https://www.acmicpc.net/problem/6376

def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num*factorial(num-1)


def e(num):
    _e = 0
    for n in range(num+1):
        fact = factorial(n)
        _e += 1/fact

    return _e


print('n e')
print('- -----------')
for i in range(10):
    res = round(e(i), 9)
    if i <= 1:
        print(i, int(res))
    elif i == 8:
        res = str(res)+str(0)
        print(i, res)
    else:
        print(i, res)
