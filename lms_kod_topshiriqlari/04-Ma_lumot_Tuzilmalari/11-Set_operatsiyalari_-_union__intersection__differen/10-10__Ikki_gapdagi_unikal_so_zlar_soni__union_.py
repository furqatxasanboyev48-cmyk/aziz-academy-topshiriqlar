s1 = input().strip().lower().split()
s2 = input().strip().lower().split()
print(len(set(s1) | set(s2)))