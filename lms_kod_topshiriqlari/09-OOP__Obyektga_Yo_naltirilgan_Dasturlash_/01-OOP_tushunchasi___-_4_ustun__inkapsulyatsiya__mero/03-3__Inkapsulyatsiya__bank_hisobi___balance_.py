class Account:
    def __init__(self, balance):
        self._balance = balance 
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return True
        return False
    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            return True
        return False
    def get_balance(self):
        return self._balance
try:
    balance = int(input().strip())
    op = input().strip()
    amount = int(input().strip())
except ValueError:
    print("BAD")
else:
    if balance < 0 or op not in ("DEPOSIT", "WITHDRAW"):
        print("BAD")
    else:
        acc = Account(balance)
        ok = acc.deposit(amount) if op == "DEPOSIT" else acc.withdraw(amount)
        print(f"BALANCE={acc.get_balance()}" if ok else "BAD")