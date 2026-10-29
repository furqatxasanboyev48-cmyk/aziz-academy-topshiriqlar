A = set(map(int, input().split()))
B = set(map(int, input().split()))
juftlar = set()
for a in A:
    for b in B:
        juftlar.add((a, b))
print(len(juftlar))
for a, b in sorted(juftlar):
    print(a, b)