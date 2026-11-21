class Bank:
    def __init__(self, balance):
        self.balance = balance 
    def deposit(self, amount):
        self.balance += amount
try:
    balance = int(input().strip())
    amount = int(input().strip())
except ValueError:
    print("BAD")
else:
    if balance >= 0 and amount > 0:
        b = Bank(balance)
        b.deposit(amount)
        print(b.balance)
    else:
        print("BAD")
        