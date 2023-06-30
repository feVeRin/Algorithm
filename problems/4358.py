import sys
from collections import Counter
input = sys.stdin.readline

trees = []
while True:
    tree = input().rstrip()
    if not tree:
        break
    trees.append(tree)

for tree, values in sorted(Counter(trees).items()):
    print('%s %.4f' %(tree, round(values/len(trees)*100, 4)))