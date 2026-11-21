class User:
    def __init__(self, username, age):
        self.username = username
        self.age = age
username = input().strip()
try:
    age = int(input().strip())
except ValueError:
    print("BAD")
else:
    if username and 0 <= age <= 120:
        u = User(username, age)
        print(f"USER={u.username} AGE={u.age}")
    else:
        print("BAD")