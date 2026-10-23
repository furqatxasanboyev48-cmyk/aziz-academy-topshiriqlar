secret = 15
while True:
    g = int(input())
    if g == secret:
        print("Correct")
        break
    elif abs(g - secret) >= 5:
        print("Far")
    else:
        print("Close")
