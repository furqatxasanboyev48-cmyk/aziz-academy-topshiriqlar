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
best = None
for product, qty, price in rows:
    total = qty * price
    if best is None or total > best[1] or (total == best[1] and product < best[0]):
        best = (product, total)
print("BEST: {} {}".format(best[0], best[1]))