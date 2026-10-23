secret = 1
c = 0
while True:
    g = int(input())
    c += 1
    if g == secret:
        print("Correct")
        break
    else:
        print("Try again")
print(c)
        