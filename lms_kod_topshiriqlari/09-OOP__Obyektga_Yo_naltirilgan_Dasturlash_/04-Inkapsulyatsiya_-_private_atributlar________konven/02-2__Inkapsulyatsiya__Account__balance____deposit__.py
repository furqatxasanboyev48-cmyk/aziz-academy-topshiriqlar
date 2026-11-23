class Account:
    def __init__(self, balance):
        self._balance = balance
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
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
        print(f"BAL={acc.get_balance()}" if acc.deposit(amount) else "BAD")
    else:
        print("BAD")