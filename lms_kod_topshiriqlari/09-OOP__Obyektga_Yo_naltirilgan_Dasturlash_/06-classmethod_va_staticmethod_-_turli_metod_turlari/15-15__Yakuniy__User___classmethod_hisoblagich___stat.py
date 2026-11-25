class User:
    count = 0
    def __init__(self, name):
        self.name = name
        User.count += 1 
    @staticmethod
    def valid(name):
        return len(name) >= 3
    @classmethod
    def total(cls):
        return cls.count 
names = input().split()
for nm in names:
    if User.valid(nm):
        User(nm)
print(User.total())
        
        