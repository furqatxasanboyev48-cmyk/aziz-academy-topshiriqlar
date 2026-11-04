def compute(a, b=1, op='+'):
    if op == '+':
        return a + b 
    if op == '-':
        return a - b 
    if op == '*':
        return a * b 
    if b == 0:
        return "ERROR"
    return a / b 
qator = input().split()
a = int(qator[0])
if len(qator) == 1:
    natija = compute(a)
elif len(qator) == 2:
    natija = compute(a, int(qator[1]))
else:
    natija = compute(a, int(qator[1]), qator[2])
if natija == "ERROR":
    print("ERROR")
elif isinstance(natija, float):
    print(f"{natija:.2f}")
else:
    print(natija)
    