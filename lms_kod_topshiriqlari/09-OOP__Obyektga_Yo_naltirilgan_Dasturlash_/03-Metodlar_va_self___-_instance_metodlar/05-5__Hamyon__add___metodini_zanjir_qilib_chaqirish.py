class Wallet:
    def __init__(self, balance):
        self.balance = balance
    def add(self, x):
        self.balance += x 
        return self 
try:
    balance = int(input().strip())
    a = int(input().strip())
    b = int(input().strip())
except ValueError:
    print("BAD")
else:
    if balance >= 0 and a >= 0 and b >= 0:
        w = Wallet(balance)
        w.add(a).add(b)
        print(w.balance)
    else:
        print("BAD")
        