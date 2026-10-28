s = input().strip()
harflar = sorted(set(s))
print("{" + ", ".join("'" + h + "'" for h in harflar) + "}")