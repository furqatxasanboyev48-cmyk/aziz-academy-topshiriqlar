n = int(input())
students = []
for _ in range(n):
    name, score = input().split()
    students.append({'name': name, 'score': int(score)})
yigindi = 0
for o in students:
    yigindi += o['score']
print(yigindi)
    