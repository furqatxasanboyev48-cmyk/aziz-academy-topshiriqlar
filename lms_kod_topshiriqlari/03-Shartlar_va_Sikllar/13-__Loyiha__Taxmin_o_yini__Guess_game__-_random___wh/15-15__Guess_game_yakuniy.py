secret = 20
c = 0
while True:
    g = int(input())
    c += 1
    if g < 1 or g > 20:
        print("Invalid")
    elif g == secret:
        print("Correct")
        break
    elif g < secret:
        print("Low")
    else:
        print("High")
print(c)
    