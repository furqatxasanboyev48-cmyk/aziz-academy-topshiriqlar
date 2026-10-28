n = int(input())
students = []
for _ in range(n):
    name, score = input().split()
    students.append({'name': name, 'score': int(score)})
ballar = []
for o in students:
    ballar.append(o['score'])
print(min(ballar))