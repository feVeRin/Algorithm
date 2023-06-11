import sys
input = sys.stdin.readline

grade_dict = {
'A+':4.5,'A0':4.0,'B+':3.5,'B0':3.0,'C+':2.5,'C0':2.0,'D+':1.5,'D0':1.0,'F':0.0
}
result = 0
count = 0

for _ in range(20):
    name, weight, grade = list(input().split())
    if grade == 'P':
        continue
    result += float(weight)*float(grade_dict[grade])
    count += float(weight)

print(result/count)