sonlar = []
while True:
    buyruq = input().split()
    if buyruq[0] == "stop":
        break
    if buyruq[0] == "append":
        sonlar.append(int(buyruq[1]))
    elif buyruq[0] == "insert":
        sonlar.insert(int(buyruq[1]), int(buyruq[2]))
    elif buyruq[0] == "remove":
        x = int(buyruq[1])
        if x in sonlar:
            sonlar.remove(x)
    elif buyruq[0] == "pop":
        sonlar.pop(int(buyruq[1]))
print(sonlar)
            
        
            
        