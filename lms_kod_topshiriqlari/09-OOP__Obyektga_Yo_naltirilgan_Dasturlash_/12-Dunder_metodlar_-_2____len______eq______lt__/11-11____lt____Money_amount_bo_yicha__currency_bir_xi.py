class Money:
    def __init__(self, amount, cur):
        self.amount = amount 
        self.cur = cur 
    def __lt__(self, other):
        return self.amount < other.amount
try:
    a_amount = int(input().strip())
    a_cur = input().strip()
    b_amount = int(input().strip())
    b_cur = input().strip()
except ValueError:
    print("BAD")
else:
    if a_cur and b_cur and a_cur == b_cur:
        print("LT" if Money(a_amount, a_cur) < Money(b_amount, b_cur) else "GE")
    else:
        print("BAD")