age = int(input())
try:
    if age < 18:
        raise ValueError("yosh")
except ValueError:
    print("DENIED")
else:
        print("ALLOWED")