# 로그의 재정렬
# 기준 1. 로그의 가장 앞부분은 식별자
# 기준 2. 문자가 숫자보다 앞에 온다
# 기준 3. 문자가 동일할 경우 식별자 순
# 기준 4. 숫자는 입력순


def reorder_log(logs: list) -> list:
    letters, digits = [], []

    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)

    letters.sort(key = lambda x: (x.split()[1:], x.split()[0]))
    return letters+digits


logs = ['dig1 8 1 5 1', 'let1 art can', 'dig2 3 6', 'let2 own kit dig', 'let3 art zero']
print(reorder_log(logs))
