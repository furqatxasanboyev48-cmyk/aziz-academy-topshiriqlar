n = int(input())
products = []
for _ in range(n):
    name, price = input().split()
    products.append({'name': name, 'price': int(price)})
narxlar = []
for p in products:
    narxlar.append(p['price'])
print(max(narxlar))