n = int(input().strip())
users = []
for _ in range(n):
    parts = input().split()
    username = parts[0]
    k = int(parts[1])
    tags = parts[2:2+k]
    users.append({'username': username, 'tags': tags})
eng = users[0]
for u in users:
    if len(u['tags']) > len(eng['tags']):
        eng = u
print(eng['username'])
