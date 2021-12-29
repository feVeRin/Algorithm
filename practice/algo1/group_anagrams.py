# 문자열 배열을 애너그램으로

import collections


s = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']


def anagram(s :list) -> list:
    anagrams = collections.defaultdict(list)

    for word in s:
        anagrams[''.join(sorted(word))].append(word)

    return anagrams.values()


print(anagram(s))