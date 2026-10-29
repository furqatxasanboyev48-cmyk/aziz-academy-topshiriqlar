sozlar = input().split()
kichik = []
for s in sozlar:
    kichik.append(s.lower())
hisob = {}
for s in kichik:
    hisob[s] = hisob.get(s, 0) + 1
eng = None
for s in sorted(hisob):
    if eng is None or hisob[s] > hisob[eng]:
        eng = s
print("total:", len(sozlar))
print("unique:", len(hisob))
print("top:", eng, hisob[eng])

