secret = 8
tries = 0
found = False
while tries < 3:
    g = int(input())
    tries += 1
    if g == secret:
        print("Correct")
        found = True
        break
if not found:
    print("Game Over")
