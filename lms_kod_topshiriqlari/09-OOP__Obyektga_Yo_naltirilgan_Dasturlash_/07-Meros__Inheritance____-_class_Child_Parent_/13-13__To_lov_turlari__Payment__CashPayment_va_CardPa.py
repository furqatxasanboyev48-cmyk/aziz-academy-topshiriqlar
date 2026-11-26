class Payment:
    def pay(self, amount):
        raise NotImplementedError
class CashPayment(Payment):
    def pay(self, amount):
        return f"CASH:{amount}"
class CardPayment(Payment):
    def pay(self, amount):
        return f"CARD:{amount}"
kind = input().strip()
try:
    amount = int(input().strip())
except ValueError:
    print("BAD")
else:
    classes = {"CASH": CashPayment, "CARD": CardPayment}
    if kind in classes and amount > 0:
        print(classes[kind]().pay(amount))
    else:
        print("BAD")
