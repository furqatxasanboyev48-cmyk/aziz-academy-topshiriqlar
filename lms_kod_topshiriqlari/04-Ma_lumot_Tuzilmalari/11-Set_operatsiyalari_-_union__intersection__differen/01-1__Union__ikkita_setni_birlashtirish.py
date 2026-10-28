a = set(map(int, input().split()))
b = set(map(int, input().split()))
u = a | b
print(" ".join(str(x) for x in sorted(u)))