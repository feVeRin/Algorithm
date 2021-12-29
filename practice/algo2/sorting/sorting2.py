N = int(input())

students = []

for _ in range(N):
    student = input().split()
    students.append((student[0], student[1]))

for s in sorted(students, key=lambda x: x[1]):
    print(s[0], end=' ')
