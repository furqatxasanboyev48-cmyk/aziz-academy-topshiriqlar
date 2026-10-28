n = int(input())
products = []
for _ in range(n):
    name, price = input().split()
    products.append({'name': name, 'price': int(price)})
x = input().strip()
bor = False
for p in products:
    if p['name'] == x:
        bor = True
if bor:
    print("YES")
else:
    print("NO")
