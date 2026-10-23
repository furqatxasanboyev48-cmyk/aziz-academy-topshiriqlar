secret = 8
first = True
while True:
    g = int(input())
    if g == secret:
        print("Correct")
        break
    if first:
        if g < secret:
            print("Low")
        else:
            print("High")
        first = False
    else:
        print("Wrong")
            