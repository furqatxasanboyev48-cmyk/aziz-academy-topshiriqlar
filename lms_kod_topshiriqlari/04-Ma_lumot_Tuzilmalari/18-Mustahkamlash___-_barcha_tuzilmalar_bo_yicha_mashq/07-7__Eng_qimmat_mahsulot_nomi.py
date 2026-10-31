n = int(input())
items = []
for _ in range(n):
    nom = input()
    narx = int(input())
    items.append({"nom": nom, "narx": narx})
best = max(items, key = lambda d: d["narx"])
print(best["nom"])