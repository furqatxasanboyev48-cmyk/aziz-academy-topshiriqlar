sonlar = list(map(int, input().split()))
s = set(sonlar)
print("{" + ", ".join(str(x) for x in sorted(s)) + "}")