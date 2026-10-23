secret = 3
while True:
    g = int(input())
    if g == 0:
        print("Exit")
        break
    elif g == secret:
        print("Correct")
        break
    elif g < secret:
        print("Low")
    else:
        print("High")