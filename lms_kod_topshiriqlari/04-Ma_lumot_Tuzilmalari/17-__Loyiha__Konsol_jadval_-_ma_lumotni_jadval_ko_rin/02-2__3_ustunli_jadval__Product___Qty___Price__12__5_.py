n = int(input())
rows = []
for _ in range(n):
    product, qty, price = input().split()
    rows.append((product, int(qty), int(price)))
print("{:<12} | {:>5} | {:>7}".format("Product", "Qty", "Price"))
print("-" * 12 + "+" + "-"* 5 + "+" + "-" * 7)
for product, qty, price in rows:
    print("{:<12} | {:>5} | {:>7}".format(product, qty, price))