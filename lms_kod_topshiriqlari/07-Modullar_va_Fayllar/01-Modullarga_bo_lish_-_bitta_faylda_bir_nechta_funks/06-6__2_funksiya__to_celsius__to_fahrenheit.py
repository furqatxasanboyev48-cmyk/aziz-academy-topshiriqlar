def to_celsius(f):
    return (f - 32) * 5 / 9
def to_fahrenheit(c):
    return c * 9 / 5 + 32
mode = input().strip()
t = float(input())
if mode == "C":
    print(f"{to_celsius(t):.2f}")
else:
    print(f"{to_fahrenheit(t):.2f}")