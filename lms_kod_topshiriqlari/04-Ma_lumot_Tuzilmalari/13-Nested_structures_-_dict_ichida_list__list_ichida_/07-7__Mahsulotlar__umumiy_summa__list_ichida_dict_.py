n = int(input().strip())
items = []
for _ in range(n):
    name, price, qty = input().split()
    items.append({'name': name, 'price': int(price), 'qty': int(qty)})
jami = 0
for it in items:
    jami += it['price'] * it['qty']
print(jami)