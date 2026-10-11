parts = input().split()
role = parts[0]
active = int(parts[1])
if role == "admin":
    if active == 1:
        print("Admin active")
    else:
        print("Admin inactive")
else:
    print("User")
        