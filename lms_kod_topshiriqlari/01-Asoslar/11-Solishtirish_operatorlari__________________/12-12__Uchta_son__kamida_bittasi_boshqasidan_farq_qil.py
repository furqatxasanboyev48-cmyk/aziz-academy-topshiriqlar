# a, b, c (bitta qatorda)
# Uchalasining hammasi teng bo'lmasa True, aks holda False.
# (a==b and b==c) bo'lmasa True
a, b, c = map(int, input().split())
print(not(a == b == c))