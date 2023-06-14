import sys
input = sys.stdin.readline

N = int(input())
company = dict()
for _ in range(N):
    name, record = map(str, input().rstrip().split())
    company[name] = record
    if record == 'leave':
        company.pop(name)

company = dict(sorted(company.items(), reverse=True))
for key in company.keys():
    print(key)