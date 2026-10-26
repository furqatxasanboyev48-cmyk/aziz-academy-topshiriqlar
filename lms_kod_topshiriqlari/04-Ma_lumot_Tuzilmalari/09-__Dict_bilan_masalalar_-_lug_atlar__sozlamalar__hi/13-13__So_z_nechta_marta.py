n = int(input())
d = {}
for _ in range(n):
    w = input()
    d[w] = d.get(w, 0) + 1
izlanadigan = input()
print(d.get(izlanadigan, 0))