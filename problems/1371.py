# https://www.acmicpc.net/problem/1371

import sys
import collections
import re

strs = re.sub(r'[\n\t\s]*', '', sys.stdin.read())
count = collections.Counter(strs)
word = []
max_c = count.most_common()[0][1]

for w, c in count.most_common():
    if c == max_c:
        word.append(w)
    else:
        break

print(''.join(sorted(word)))
