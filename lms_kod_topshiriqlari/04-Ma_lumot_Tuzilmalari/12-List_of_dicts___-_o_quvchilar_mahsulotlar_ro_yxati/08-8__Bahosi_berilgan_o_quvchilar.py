n = int(input())
students = []
for _ in range(n):
    name, score = input().split()
    students.append({'name': name, 'score': int(score)})
x = int(input())
soni = 0
for o in students:
    if o['score'] == x:
        soni += 1
print(soni)