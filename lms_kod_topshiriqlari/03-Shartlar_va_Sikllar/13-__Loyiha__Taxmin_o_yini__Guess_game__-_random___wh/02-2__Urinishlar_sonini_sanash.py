secret = 5
c = 0
while True:
    g = int(input())
    c += 1
    if g == secret:
        break
print(c)