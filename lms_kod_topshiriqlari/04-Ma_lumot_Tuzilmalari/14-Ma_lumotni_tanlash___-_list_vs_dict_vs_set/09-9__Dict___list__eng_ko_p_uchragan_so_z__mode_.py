sozlar = input().lower().split()
hisob = {}
for s in sozlar:
    hisob[s] = hisob.get(s, 0) +1
eng = None
for s in sorted(hisob):
    if eng is None or hisob[s] > hisob[eng]:
        eng = s
print(eng, hisob[eng])