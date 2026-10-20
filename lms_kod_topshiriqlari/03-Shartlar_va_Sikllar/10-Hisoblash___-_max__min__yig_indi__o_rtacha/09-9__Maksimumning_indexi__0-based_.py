n = int(input())
parts = input().split()
lst = []
for p in parts:
    lst.append(int(p))
mi = 0
for i in range(len(lst)):
    if lst[i] > lst[mi]:
        mi = i
print(mi)
