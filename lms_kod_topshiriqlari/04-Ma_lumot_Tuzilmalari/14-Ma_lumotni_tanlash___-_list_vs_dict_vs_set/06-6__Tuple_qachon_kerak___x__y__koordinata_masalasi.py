n = int(input())
nuqtalar = []
for _ in range(n):
    x, y = map(int, input().split())
    nuqtalar.append((x, y))
eng = nuqtalar[0]
for p in nuqtalar:
    if p[0] > eng[0] or (p[0] == eng[0] and p[1] < eng[1]):
        eng = p
print(eng[0], eng[1])
