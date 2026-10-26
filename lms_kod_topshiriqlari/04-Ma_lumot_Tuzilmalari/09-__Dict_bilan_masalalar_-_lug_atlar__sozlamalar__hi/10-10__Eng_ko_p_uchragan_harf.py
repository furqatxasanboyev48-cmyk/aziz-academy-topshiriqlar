s = input()
d = {}
for ch in s:
    if ch in d:
        d[ch] += 1
    else:
        d[ch] = 1
eng = None
mx = -1
for ch in d:
    if d[ch] > mx:
        mx = d[ch]
        eng = ch
print(eng)