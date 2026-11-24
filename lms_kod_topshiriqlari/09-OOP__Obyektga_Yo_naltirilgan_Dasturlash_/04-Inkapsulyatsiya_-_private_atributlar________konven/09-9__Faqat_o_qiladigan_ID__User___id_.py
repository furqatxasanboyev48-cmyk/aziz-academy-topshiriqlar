class User:
    def __init__(self,user_id):
        self.__id = user_id
    @property
    def id(self):
        return self.__id
try:
    user_id = int(input().strip())
except ValueError:
    print("BAD")
else:
    if user_id > 0:
        print(f"ID={User(user_id).id}")
    else:
        print("BAD")