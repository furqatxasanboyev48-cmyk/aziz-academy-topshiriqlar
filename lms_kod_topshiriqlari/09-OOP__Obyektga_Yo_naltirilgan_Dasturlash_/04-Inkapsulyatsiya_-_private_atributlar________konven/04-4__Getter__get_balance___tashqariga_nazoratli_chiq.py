class Account:
    def __init__(self, balance):
        self._balance = balance
    def get_balance(self):
        return self._balance
try:
    balance = int(input().strip())
except ValueError:
    print("BAD")
else:
    if balance >= 0:
        print(Account(balance).get_balance())
    else:
        print("BAD")