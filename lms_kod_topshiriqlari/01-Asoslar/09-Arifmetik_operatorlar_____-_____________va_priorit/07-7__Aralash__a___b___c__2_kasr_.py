# a, b, c (bitta qatorda)
# a + (b / c) ni hisoblang va 2 kasr bilan chiqaring.
# "Result: <natija>"
a, b, c = input().split()
natija = int(a) + (int(b) / int(c))
print(f"Result: {natija:.2f}")