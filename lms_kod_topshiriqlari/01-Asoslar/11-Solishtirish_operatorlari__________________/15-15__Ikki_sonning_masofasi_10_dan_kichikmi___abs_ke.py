# a va b (butun sonlar, bitta qatorda)
# Farqning moduli 10 dan kichik bo'lsa True.
# abs ishlatmasdan: (a-b < 10) and (a-b > -10)
a, b = map(int, input().split())
print((a - b < 10) and (a - b > -10))