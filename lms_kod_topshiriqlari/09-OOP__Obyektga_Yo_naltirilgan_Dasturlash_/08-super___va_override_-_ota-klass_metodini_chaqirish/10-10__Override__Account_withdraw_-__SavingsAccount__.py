class Account:
    def __init__(self, balance):
        self.balance = balance
    def withdraw(self, x):
        self.balance -= x 
        return self.balance
class Savings(Account):
    def withdraw(self, x):
        if self.balance - x < 100:
            return self.balance
        return super().withdraw(x)
b, x = map(int, input().split())  
print(Savings(b).withdraw(x))