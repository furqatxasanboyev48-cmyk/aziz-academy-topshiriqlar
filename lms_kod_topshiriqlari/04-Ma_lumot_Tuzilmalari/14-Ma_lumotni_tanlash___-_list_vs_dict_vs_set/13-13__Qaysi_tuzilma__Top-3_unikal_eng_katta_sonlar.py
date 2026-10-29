sonlar = list(map(int, input().split()))
unikal = sorted(set(sonlar), reverse=True)
print(" ".join(str(x) for x in unikal[:3]))