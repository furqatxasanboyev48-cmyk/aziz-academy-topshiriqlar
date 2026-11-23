class Account:
    def __init__(self, balance):
        self._balance = balance
    def withdraw(self, amount):
        if amount > 0 and self._balance >= amount:
            self._balance -= amount
            return True
        return False
    def get_balance(self):
        return self._balance
try:
    balance = int(input().strip())
    amount = int(input().strip())
except ValueError:
    print("BAD")
else:
    if balance >= 0:
        acc = Account(balance)
        print(f"BAL={acc.get_balance()}" if acc.withdraw(amount) else "BAD")
    else:
        print("BAD")
        
        