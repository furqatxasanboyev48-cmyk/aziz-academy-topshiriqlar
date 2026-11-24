class MiniBank:
    def __init__(self, balance):
        self.__balance = balance
    @property
    def balance(self):
        return self.__balance
    def deposit(self, x):
        if x > 0:
            self.__balance += x 
            return True
        return False
    def withdraw(self, x):
        if x > 0 and self.__balance >= x:
            self.__balance -= x 
            return True
        return False
try:
    balance = int(input().strip())
    q = int(input().strip())
    if balance < 0 or q < 0:
        raise ValueError
    bank = MiniBank(balance)
    for _ in range(q):
        parts = input().split()
        if len(parts) != 2:
            raise ValueError
        cmd, amount = parts[0], int(parts[1]) 
        if cmd == "DEP":
            ok = bank.deposit(amount)
        elif cmd == "WDR":
            ok = bank.withdraw(amount)
        else:
            ok = False
        if not ok:
            raise ValueError
    print(f"BAL={bank.balance}")
except ValueError:
    print("BAD")