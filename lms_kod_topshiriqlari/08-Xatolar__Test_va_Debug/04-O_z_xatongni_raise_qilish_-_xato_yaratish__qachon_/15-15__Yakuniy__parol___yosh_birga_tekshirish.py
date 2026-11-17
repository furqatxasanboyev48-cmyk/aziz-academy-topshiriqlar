age = int(input())
password = input()
try:
    if age < 18:
        raise ValueError("yosh")
    if len(password) < 6:
        raise ValueError("parol")
except ValueError:
    print("REJECT")
else:
    print("ACCEPT")
