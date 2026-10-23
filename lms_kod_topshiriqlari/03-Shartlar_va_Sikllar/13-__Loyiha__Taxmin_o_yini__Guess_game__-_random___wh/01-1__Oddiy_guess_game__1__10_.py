secret = 7
while True:
    g = int(input())
    if g < secret:
        print("Low")
    elif g > secret:
        print("High")
    else:
        print("Correct")
        break