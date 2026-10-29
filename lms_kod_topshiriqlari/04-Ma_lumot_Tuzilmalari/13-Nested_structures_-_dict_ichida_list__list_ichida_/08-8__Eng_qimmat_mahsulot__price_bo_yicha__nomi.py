n = int(input().strip())
items = []
for _ in range(n):
    name, price, qty = input().split()
    items.append({'name': name, 'price': int(price), 'qty': int(qty)})
eng = items[0]
for it in items:
    if it['price'] > eng['price']:
        eng = it
print(eng['name'])
