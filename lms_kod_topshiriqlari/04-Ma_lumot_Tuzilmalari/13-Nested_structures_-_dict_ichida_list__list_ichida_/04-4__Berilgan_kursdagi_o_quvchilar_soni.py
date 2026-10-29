n = int(input().strip())
courses = []
for _ in range(n):
    parts = input().split()
    name = parts[0]
    k = int(parts[1])
    students = parts[2:2+k]
    courses.append({'name': name, 'students': students})

target = input().strip()
soni = 0
for c in courses:
    if c['name'] == target:
        soni = len(c['students'])
print(soni)