def squares(n):
    natija = []
    for i in range(1, n + 1):
        natija.append(i * i)
    return natija
n = int(input())
print(" ".join(str(x) for x in squares(n)))
    
        
    