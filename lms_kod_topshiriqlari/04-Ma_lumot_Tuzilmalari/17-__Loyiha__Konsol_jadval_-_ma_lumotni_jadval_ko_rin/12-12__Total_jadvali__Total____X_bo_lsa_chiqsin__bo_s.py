n = int(input())
rows = []
for _ in range(n):
    product, qty, price = input().split()
    rows.append((product, int(qty), int(price)))
x = int(input())
print("{:<12} | {:>5} | {:>7} | {:>9}".format("Product", "Qty", "Price", "Total"))
print("-" * 12 + "+" + "-" * 5 + "+" + "-" * 7 + "+" + "-" * 9)
tanlangan = []
for product, qty, price in rows:
    total = qty * price
    if total >= x:
        tanlangan.append((product, qty, price, total))
if tanlangan:
    for product, qty, price, total in tanlangan:
        print("{:<12} | {:>5} | {:>7} | {:>9}".format(product, qty, price, total))
else:
    print("EMPTY")
    
        
