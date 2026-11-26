class BaseUser:
    def __init__(self, username):
        self.username = username
class AdminUser(BaseUser):
    def __init__(self, username, level):
        super().__init__(username)
        self.level = level
    def info(self):
        return f"{self.username} level={self.level}"
username = input().strip()
try:
    level = int(input().strip())
except ValueError:
    print("BAD")
else:
    if username and 1 <= level <= 10:
        print(AdminUser(username, level).info())
    else:
        print("BAD")