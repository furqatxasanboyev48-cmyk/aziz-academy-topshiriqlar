bolaklar = input().split()
elementlar = []
for b in bolaklar:
    if b.lstrip("-").isdigit():
        elementlar.append(int(b))
    elif b.replace(".", "", 1).lstrip("-").isdigit():
        elementlar.append(float(b))
    else:
        elementlar.append(b)
print(tuple(elementlar))
        