n = int (input())
for d in range(2, n + 1):
    if n % d == 0:
        prime = True
        for j in range(2, d):
            if d % j == 0:
                prime = False
                break
        if prime:
            print(d)