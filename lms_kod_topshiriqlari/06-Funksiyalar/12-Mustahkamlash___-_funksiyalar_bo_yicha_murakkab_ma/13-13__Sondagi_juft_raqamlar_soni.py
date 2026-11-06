n = input().strip()
print(sum(1 for c in n if int(c) % 2 == 0))