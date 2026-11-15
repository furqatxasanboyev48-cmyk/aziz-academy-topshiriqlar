secret = int(input())
attempts = 0
while True:
    guess = int(input())
    attempts += 1
    if guess == secret:
        print("TOPDINGIZ")
        break
    elif guess > secret:
        print("KATTA")
    else:
        print("KICHIK")
print(f"Urinishlar: {attempts}")
    
    