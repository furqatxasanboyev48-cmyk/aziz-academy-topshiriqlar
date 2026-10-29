n = int(input().strip())
courses = []
for _ in range(n):
    parts = input().split()
    name = parts[0]
    k = int(parts[1])
    students = parts[2:2+k]
    courses.append({'name': name, 'students': students})
eng = courses[0]
for c in courses:
    if len(c['students']) > len(eng['students']):
        eng = c
print(eng['name'])