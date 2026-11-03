def calc_discount(price, percent):
    return price - price * percent / 100
qator = input().split()
price = int(qator[0])
percent = int(qator[1])
n1 = calc_discount(price, percent)
n2 = calc_discount(percent=percent, price=price)
print(f"{n1:.2f}")
print(f"{n2:.2f}")