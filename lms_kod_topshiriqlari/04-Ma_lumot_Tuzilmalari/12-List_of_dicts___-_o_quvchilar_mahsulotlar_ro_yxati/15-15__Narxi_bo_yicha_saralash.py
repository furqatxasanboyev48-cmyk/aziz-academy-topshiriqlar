n = int(input())
products = []
for _ in range(n):
    name, price = input().split()
    products.append({'name': name, 'price': int(price)})
def narxi(p):
    return p['price']
products.sort(key=narxi)
for p in products:
    print(p['name'], p['price'])