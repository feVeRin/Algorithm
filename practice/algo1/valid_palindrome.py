# palindrome : 앞뒤가 같은 문자열
# Q : 주어진 문자열이 팰린드롬인지 확인하라

sent = str(input()).lower()


def palind(sent):
    new_sent = []
    for s in sent:
        if s.isalpha():  # <--- s.isalnum()으로 수정되어야 함(영숫자 가능) // isalpha()는 영어만 걸러냄
            new_sent.append(s)

    if new_sent == new_sent[::-1]:  # 앞뒤가 같으면(문자열 슬라이싱 이용)
        return True

    return False


print(palind(sent))
