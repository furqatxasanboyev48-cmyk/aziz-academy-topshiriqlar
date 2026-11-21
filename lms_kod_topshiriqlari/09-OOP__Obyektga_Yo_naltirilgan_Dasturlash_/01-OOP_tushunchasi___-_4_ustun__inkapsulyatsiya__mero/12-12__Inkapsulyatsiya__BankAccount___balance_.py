class BankAccount:
    def __init__(self, balance):
        self._balance = balance
    def deposit(self, x):
        self._balance += x 
    def withdraw(self, x):
        if x <= self._balance:
            self._balance -= x 
    def balance(self):
        return self._balance
b, d, w = map(int, input().split())
acc = BankAccount(b)
acc.deposit(d)
acc.withdraw(w)
print(acc.balance())
              
            
        