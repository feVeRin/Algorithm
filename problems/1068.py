import sys
input = sys.stdin.readline

def dfs(remove, tree):
    tree[remove] = -2
    for i in range(len(tree)):
        if remove == tree[i]:
            dfs(i, tree)

if __name__ == '__main__':
    N = int(input())
    tree = list(map(int, input().split()))
    remove = int(input())

    dfs(remove, tree)
    count = 0
    for i in range(len(tree)):
        if tree[i] != -2 and i not in tree:
            count += 1
    print(count)