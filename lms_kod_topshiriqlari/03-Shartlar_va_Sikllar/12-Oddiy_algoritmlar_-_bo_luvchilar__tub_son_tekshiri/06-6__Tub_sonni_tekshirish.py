n = int(input())
if n < 2:
    print("Composite")
else:
    prime = True
    for i in range(2, n):
        if n % i == 0:
            prime = False
            break
    if prime:
        print("Prime")
    else:
        print("Composite")