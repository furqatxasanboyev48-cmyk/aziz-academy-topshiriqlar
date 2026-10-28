A = set(input().strip().split())
B = set(input().strip().split())
umumiy = A & B 
print(len(umumiy))
for ism in sorted(umumiy):
    print(ism)