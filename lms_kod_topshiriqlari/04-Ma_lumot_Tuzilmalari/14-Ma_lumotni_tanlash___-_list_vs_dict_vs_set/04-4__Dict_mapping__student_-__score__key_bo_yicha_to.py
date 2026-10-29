n = int(input())
baholar = {}
for _ in range(n):
    name, score = input().split()
    baholar[name] = int(score)
q = int(input())
for _ in range(q):
    name = input().strip()
    if name in baholar:
        print(baholar[name])
    else:
        print("NOT_FOUND")
        