sonlar = sorted(map(int, input().split()), reverse=True)
print(" ".join(str(x) for x in sonlar[:3]))