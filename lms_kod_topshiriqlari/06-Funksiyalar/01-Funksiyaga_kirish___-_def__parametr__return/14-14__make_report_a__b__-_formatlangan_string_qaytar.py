def make_report(a, b):
    return f"sum: {a + b}\ndiff: {a - b}\nprod: {a * b}"
qator = input().split()
a = int(qator[0])
b = int(qator[1])
print(make_report(a, b))