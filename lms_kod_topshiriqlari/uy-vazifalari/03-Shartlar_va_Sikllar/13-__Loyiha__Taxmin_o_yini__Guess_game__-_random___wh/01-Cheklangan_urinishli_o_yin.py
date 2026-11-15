secret = int(input())
n = int(input())
found = False
for _ in range(n):
    guess = int(input())
    if guess == secret:
        print("TOPDINGIZ")
        found = True
        break
    elif guess > secret:
        print("KATTA")
    else:
        print("KICHIK")
if not found:
    print("YUTQAZDINGIZ")
        