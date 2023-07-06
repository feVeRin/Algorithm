import sys
sys.setrecursionlimit(10 ** 9)


def postorder(start, end):
    if start > end:
        return

    division = end + 1
    for i in range(start + 1, end + 1):
        if post[start] < post[i]:
            division = i
            break

    postorder(start + 1, division - 1)
    postorder(division, end)
    print(post[start])


post = []
count = 0
while count < 10001:
    try:
        num = int(input())
    except:
        break
    post.append(num)
    count += 1

postorder(0, len(post) - 1)
