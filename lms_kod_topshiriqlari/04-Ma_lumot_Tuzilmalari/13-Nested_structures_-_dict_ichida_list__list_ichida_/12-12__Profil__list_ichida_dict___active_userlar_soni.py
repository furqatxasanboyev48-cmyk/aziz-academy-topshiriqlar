n = int(input().strip())
users = []
for _ in range(n):
    username, active = input().split()
    users.append({'username': username, 'active': active == '1'})
soni = 0
for u in users:
    if u['active']:
        soni += 1
print(soni)
