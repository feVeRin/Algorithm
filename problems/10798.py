# https://www.acmicpc.net/problem/10798

strs, res = [], []
maxlen = 0

for i in range(5):
    st = input()
    strs.append(st)
    maxlen = max(len(st), maxlen)


for i in range(maxlen):
    for j in range(len(strs)):
        try:
            res.append(strs[j][i])
        except:
            pass

print(''.join(res))
