class Money:
    def __init__(self, amount, cur):
        self.amount = amount
        self.cur = cur 
    def __eq__(self, other):
        return self.amount == other.amount and self.cur == other.cur
try:
    a_amount = int(input().strip())
    a_cur = input().strip()
    b_amount = int(input().strip())
    b_cur = input().strip()
except ValueError:
    print("BAD")
else:
    if a_cur and b_cur:
        print("EQ" if Money(a_amount, a_cur) == Money(b_amount, b_cur) else "NEQ")
    else:
        print("BAD")