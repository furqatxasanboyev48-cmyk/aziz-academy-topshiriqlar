n = int(input())
d = {}
for _ in range(n):
    w = input()
    if w in d:
        d[w] += 1
    else:
        d[w] = 1
eng = None
max_son = -1
for w in d:
    if d[w] > max_son:
        max_son = d[w]
        eng = w
print(eng)