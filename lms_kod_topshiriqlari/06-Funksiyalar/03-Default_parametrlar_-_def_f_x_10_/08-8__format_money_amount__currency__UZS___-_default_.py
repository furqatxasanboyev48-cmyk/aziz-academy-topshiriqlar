def format_money(amount, currency="UZS"):
    return f"{amount} {currency}"
qator = input().split()
if len(qator) == 1:
    print(format_money(int(qator[0])))
else:
    print(format_money(int(qator[0]), qator[1]))