sozlar = input().split()
hisob = {}
for s in sozlar:
    s = s.lower()
    hisob[s] = hisob.get(s, 0) + 1
for s in sorted(hisob):
    print(s, hisob[s])