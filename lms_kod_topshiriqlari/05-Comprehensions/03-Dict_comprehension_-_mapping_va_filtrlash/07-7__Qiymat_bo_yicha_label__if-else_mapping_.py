n = int(input())
d = {}
for _ in range(n):
    kalit, qiymat = input().split()
    d[kalit] = int(qiymat)
natija = {k: "even" if v % 2 == 0 else "odd" for k, v in d.items()}
print(natija)