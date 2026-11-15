secret = int(input())
guess = int(input())
if guess == secret:
    print("TOPDINGIZ")
elif guess > secret:
    print("KATTA")
else:
    print("KICHIK")