vaqt = input().strip()
h, m, s = vaqt.split(":")
total = int(h) * 3600 + int(m) * 60 + int(s)
print(total)