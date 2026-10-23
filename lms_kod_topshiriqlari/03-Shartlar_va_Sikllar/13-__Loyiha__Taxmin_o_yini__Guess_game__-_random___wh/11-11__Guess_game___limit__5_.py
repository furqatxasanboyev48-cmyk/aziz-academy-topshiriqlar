secret = 10
tries = 0
found = False
while tries < 5:
    g = int(input())
    tries += 1
    if g == secret:
        print("Correct")
        found = True
        break
if not found:
    print("You lost")