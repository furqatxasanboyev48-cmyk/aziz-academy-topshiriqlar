class Account:
    def __init__(self, balance):
        self._balance = balance
    def set_balance(self, x):
        if x >= 0:
            self._balance = x 
            return True
        return False
    def get_balance(self):
        return self._balance
try:
    balance = int(input().strip())
    new_balance = int(input().strip())
except ValueError:
    print("BAD")
else:
    if balance >= 0:
        acc = Account(balance)
        print(f"BAL={acc.get_balance()}" if acc.set_balance(new_balance) else "BAD")
    else:
        print("BAD")