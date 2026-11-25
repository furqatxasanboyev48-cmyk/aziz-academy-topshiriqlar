class Money:
    def __init__(self, dollars, cents):
        self.dollars= dollars
        self.cents = cents
    @classmethod
    def from_cents(cls, total):
        return cls(total // 100, total % 100)
    def show(self):
        return f"${self.dollars}.{self.cents:02d}"
print(Money.from_cents(int(input())).show())