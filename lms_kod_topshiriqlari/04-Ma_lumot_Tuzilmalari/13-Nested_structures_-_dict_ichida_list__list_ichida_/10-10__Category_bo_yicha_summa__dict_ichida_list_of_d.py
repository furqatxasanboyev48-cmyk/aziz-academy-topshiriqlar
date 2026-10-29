n = int(input().strip())
items = []
for _ in range(n):
    cat, name, price, qty = input().split()
    items.append({'cat': cat, 'name': name, 'price': int(price), 'qty': int(qty)})
summalar = {}
for it in items:
    summalar[it['cat']] = summalar.get(it['cat'], 0) + it['price'] * it['qty']
for cat in sorted(summalar):
        print(cat, summalar[cat])
    