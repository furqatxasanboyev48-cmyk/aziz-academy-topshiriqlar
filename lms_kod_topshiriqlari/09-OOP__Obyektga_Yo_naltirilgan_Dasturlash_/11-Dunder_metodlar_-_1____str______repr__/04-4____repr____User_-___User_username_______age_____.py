class User:
    def __init__(self, username, age):
        self.username = username
        self.age = age
    def __repr__(self):
        return f"User(username='{self.username}', age={self.age})"
username = input().strip()    
try:
    age = int(input().strip())
except ValueError:
    print("BAD")
else:
    if username and 0 <= age <= 120:
        print(repr(User(username, age)))
    else:
        print("BAD")