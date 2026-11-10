s = int(input())
h = s // 3600
m = (s % 3600) // 60
sek = s % 60
print(f"{h}h {m}m {sek}s")