secret = 4
c = 0
while True:
    g = int(input())
    c += 1
    if g == secret:
        print("Correct in", c, "tries")
        break