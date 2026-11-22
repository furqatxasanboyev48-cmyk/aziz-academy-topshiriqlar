class Bank:
    def __init__(self, balance):
        self.balance = balance
    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            return True
        return False
try:
    balance = int(input().strip())
    amount = int(input().strip())
except ValueError:
    print("BAD")
else:
    if balance >= 0:
        b = Bank(balance)
        print(f"BAL={b.balance}" if b.withdraw(amount) else "BAD")
    else:
        print("BAD")