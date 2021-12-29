# 금지어를 제외한 가장 흔하게 등장하는 단어를 찾아라

from collections import Counter
import re


paragraph = 'bob hit a ball the hit ball flew far afteer it was hit.'
banned = ['hit']


def common_word(para : str, ban : list) -> str:
    words = [word for word in re.sub(r'[^\w]', ' ', para).lower().split() if word not in ban]
    count = Counter(words)
    return count.most_common(1)[0][0]


print(common_word(paragraph, banned))
