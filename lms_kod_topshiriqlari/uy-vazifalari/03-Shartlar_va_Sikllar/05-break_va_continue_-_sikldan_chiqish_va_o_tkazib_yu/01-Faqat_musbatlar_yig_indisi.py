n = int(input())
i = 0
s = 0
while i < n:
    x = int(input())
    i = i + 1
    if x <= 0:
        continue
    s = s + x
print(s)