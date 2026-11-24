class Wallet:
    def __init__(self, balance):
        self._balance = balance 
    def deposit(self, x):
        if x > 0:
            self._balance += x 
    def withdraw(self, x):
        if 0 < x <= self._balance:
            self._balance -= x 
    @property
    def balance(self):
        return self._balance
b, d, w = map(int, input().split())
wal = Wallet(b)
wal.deposit(d)
wal.withdraw(w)
print(wal.balance)

        
        