def tax(price, rate=12):
    return price * (1 + rate / 100)
qator = input().split()
if len(qator) == 1:
    natija = tax(int(qator[0]))
else:
    natija = tax(int(qator[0]), int(qator[1]))
print(f"{natija:.2f}")
    