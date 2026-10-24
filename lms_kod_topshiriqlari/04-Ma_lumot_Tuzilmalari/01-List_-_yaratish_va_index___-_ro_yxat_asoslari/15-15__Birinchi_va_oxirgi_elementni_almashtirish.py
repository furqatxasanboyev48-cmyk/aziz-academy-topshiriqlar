n = int(input())
sonlar = list(map(int, input().split()))
vaqtincha = sonlar[0]
sonlar[0] = sonlar[-1]
sonlar[-1] = vaqtincha
print(sonlar)