sonlar = sorted(map(int, input().split()))
n = len(sonlar)
if n % 2 == 1:
    median = sonlar[n // 2]
else:
    median = (sonlar[n // 2 - 1] + sonlar[n // 2]) / 2
print("{:.2f}".format(median))
