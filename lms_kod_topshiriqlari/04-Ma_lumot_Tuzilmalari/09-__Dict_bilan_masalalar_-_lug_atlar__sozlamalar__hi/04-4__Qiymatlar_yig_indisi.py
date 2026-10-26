n = int(input())
d = {}
for i in range(n):
    d["k" + str(i)] = int(input())
print(sum(d.values()))