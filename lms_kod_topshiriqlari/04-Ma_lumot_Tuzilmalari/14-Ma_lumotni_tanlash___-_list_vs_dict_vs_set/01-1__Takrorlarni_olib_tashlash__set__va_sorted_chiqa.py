sonlar = list(map(int, input().split()))
unikal = sorted(set(sonlar))
print(" ".join(str(x) for x in unikal))