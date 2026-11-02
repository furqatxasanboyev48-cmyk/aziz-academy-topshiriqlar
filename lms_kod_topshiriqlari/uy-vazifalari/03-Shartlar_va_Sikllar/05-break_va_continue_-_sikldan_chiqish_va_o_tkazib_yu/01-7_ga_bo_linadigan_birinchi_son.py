n = int(input())
i = 0
found = 0
ok = 0
while i < n:
    x = int(input())
    i = i + 1
    if x % 7 == 0:
        found = x
        ok = 1
        break
if ok == 1:
    print(found)
else:
    print("yo'q")