n = int(input())
sonlar = list(map(int, input().split()))
if len(sonlar) > 5:
    print(sonlar[5])
else:
    print("Error")