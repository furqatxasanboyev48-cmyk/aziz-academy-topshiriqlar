email = input()
parol = input()
print("@" in email and "." in email and len(parol) >= 8 and len(parol) <= 16 and email == email.lower())