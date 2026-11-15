secret = int(input())
k = int(input())
for _ in range(k):
    guess = int(input())
    if guess == secret:
        print("TOPDINGIZ")
    elif guess > secret:
        print("KATTA")
    else:
        print("KICHIK")