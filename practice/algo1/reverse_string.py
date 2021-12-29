# 문자열을 뒤집는 함수를 작성하라


def reverse_str(strs : list) -> None:
    strs.reverse()


strs = list(input().split())
reverse_str(strs)
print(strs)