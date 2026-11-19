def faktorial(n):
    natija = 1
    for i in range(1, n + 1):
        natija *= i 
    return natija
n = int(input())
print(faktorial(n))
    