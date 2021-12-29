strs = list(str(input()))

new = []
new2 = 0

for s in sorted(strs):
    if s.isalpha():
        new.append(s)
    else:
        new2 += int(s)

new.append(str(new2))
print(''.join(new))
