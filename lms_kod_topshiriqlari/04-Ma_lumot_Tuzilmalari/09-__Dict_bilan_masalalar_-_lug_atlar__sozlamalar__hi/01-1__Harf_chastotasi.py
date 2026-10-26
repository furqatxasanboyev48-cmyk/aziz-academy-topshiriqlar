s = input()
d = {}
for ch in s:
    if ch in d:
        d[ch] += 1
    else:
        d[ch] = 1
qismlar = []
for ch in d:
    qismlar.append(ch + ":" + str (d[ch]))
print(" ".join(qismlar))
    