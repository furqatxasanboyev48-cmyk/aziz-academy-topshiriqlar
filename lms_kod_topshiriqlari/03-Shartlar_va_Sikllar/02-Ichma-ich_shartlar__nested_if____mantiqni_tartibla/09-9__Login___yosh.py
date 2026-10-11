parts = input().split()
username = parts[0]
age = int(parts[1])
if username == "admin":
    if age >= 18:
        print("Full access")
    else:
        print("Limited")
else:
    print("No access")
