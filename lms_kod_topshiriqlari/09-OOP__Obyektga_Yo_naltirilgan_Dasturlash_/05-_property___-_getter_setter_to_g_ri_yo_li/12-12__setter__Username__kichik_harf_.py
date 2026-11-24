class User:
    def __init__(self):
        self._username = ""
    @property
    def username(self):
        return self._username
    @username.setter
    def username(self, v):
        self._username = v.lower()
u = User()        
u.username = input()
print(u.username)