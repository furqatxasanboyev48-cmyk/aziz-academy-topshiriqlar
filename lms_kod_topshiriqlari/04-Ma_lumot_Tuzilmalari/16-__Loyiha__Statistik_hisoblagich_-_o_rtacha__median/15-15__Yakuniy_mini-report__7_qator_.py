sonlar = list(map(int, input().split()))
juftlar = 0
toqlar = 0
for x in sonlar:
    if x % 2 == 0:
        juftlar += 1
    else:
        toqlar += 1
mean = sum(sonlar) / len(sonlar)
print("count:",len(sonlar))
print("sum:", sum(sonlar))
print("min:", min(sonlar))
print("max:", max(sonlar))
print("mean: {:.2f}".format(mean))
print("evens:", juftlar)
print("odds:", toqlar)

