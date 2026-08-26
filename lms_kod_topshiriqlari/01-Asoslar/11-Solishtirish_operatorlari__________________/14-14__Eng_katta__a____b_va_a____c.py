# a, b, c (bitta qatorda)
# a eng katta yoki teng (ya'ni a>=b va a>=c) bo'lsa True, aks holda False.
a, b, c = map(int, input().split())
print(a >= b and a >= c)