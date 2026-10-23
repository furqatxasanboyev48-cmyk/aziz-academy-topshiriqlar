secret = 6
while True:
    g = int(input())
    if g < 1 or g > 10:
        print("Invalid")
        continue
    if g == secret:
        print("Correct")
        break