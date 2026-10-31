ism = input()
ballar = [int(x) for x in input().split()]
d = {ism: ballar}
print(sum(d[ism]))