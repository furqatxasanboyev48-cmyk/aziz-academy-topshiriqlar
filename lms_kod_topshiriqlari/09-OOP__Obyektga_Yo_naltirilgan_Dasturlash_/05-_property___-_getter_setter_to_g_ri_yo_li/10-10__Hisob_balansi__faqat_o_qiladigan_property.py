class Account:
    def __init__(self, balance):
        self._balance = balance 
    def deposit(self, x):
        self._balance += x 
    @property
    def balance(self):
        return self._balance
b, d = map(int, input().split())    
a =Account(b)
a.deposit(d)
print(a.balance)