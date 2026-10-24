sonlar = [1, 2, 3]
x = int(input())
if x in sonlar:
    sonlar.remove(x)
    print("Removed")
else:
    print("Not found")
print(sonlar)