class Password:
    def __init__(self, pwd):
        self.__pwd = pwd
    def set_password(self, x):
        self.__pwd = x 
    def check(self, x):
        return self.__pwd == x 
password = input().strip()
new_password = input().strip()
if len(password) >= 6 and len(new_password) >= 6:
    p = Password(password)
    print("OK" if p.check(new_password) else "NO")
else:
    print("BAD")