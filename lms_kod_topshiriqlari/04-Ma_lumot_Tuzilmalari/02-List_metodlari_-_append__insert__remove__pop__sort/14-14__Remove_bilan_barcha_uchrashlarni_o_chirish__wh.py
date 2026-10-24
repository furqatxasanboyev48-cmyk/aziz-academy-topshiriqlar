n = int(input())
sonlar = list(map(int, input().split()))
x = int(input())
while x in sonlar:
    sonlar.remove(x)
print(sonlar)