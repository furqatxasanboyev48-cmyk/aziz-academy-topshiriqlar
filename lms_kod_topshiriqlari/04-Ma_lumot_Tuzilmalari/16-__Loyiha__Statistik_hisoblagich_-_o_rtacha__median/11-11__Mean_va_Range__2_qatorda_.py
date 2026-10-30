sonlar = list(map(int, input().split()))
mean = sum(sonlar) / len(sonlar)
print("{:.2f}".format(mean))
print(max(sonlar) - min(sonlar))