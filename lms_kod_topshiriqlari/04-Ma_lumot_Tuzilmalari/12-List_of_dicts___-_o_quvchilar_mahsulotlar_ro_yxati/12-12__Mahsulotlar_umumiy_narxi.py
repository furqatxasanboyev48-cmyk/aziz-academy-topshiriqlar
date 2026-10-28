n = int(input())
products = []
for _ in range(n):
    name, price = input().split()
    products.append({'name': name, 'price': int(price)})
jami = 0
for p in products:
    jami += p['price']
print(jami)