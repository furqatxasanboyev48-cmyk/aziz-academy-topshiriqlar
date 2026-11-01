a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
juftlar = {(x, y) for x in a for y in b}
print(len(juftlar))
for x, y in sorted(juftlar):
    print(f"{x},{y}")