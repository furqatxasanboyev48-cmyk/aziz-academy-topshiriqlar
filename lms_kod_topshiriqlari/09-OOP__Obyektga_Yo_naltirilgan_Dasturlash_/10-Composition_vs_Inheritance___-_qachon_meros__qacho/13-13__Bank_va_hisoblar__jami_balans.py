class Account:
    def __init__(self, balance):
        self.balance = balance
class Bank:
    def __init__(self):
        self.accounts = []
    def add(self, a):
        self.accounts.append(a)
    def total(self):
        return sum(a.balance for a in self.accounts)
bs = list(map(int, input().split()))    
bank = Bank()
for b in bs:
    bank.add(Account(b))
print(bank.total())
