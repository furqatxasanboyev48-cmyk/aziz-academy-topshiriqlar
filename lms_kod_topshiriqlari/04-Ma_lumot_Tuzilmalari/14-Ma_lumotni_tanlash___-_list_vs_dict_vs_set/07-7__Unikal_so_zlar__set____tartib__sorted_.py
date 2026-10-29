sozlar = input().lower().split()
unikal = sorted(set(sozlar))
print(" ".join(unikal))