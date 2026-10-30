n = int(input())
rows = []
for _ in range(n):
    product, qty, price = input().split()
    rows.append((product, int(qty), int(price)))
print("{:<12} | {:>5} | {:>7} | {:>9}".format("Product", "Qty", "Price", "Total"))
print("-" * 12 + "+" + "-" * 5 + "+" + "-" * 7 + "+" + "-" * 9)
for product, qty, price in rows:
    total = qty * price
    print("{:<12} | {:>5} | {:>7} | {:>9}".format(product, qty, price, total))
grand = 0
for product, qty, price in rows:
    grand += qty * price
print("GRAND: {}".format(grand))
   