def to_int(s, default=0):
    try:
        return int(s)
    except ValueError:
        return default
def to_float(s, default=0.0):
    try:
        return float(s)
    except ValueError:
        return default
s1 = input()
s2 = input()
print(to_int(s1))
print(f"{to_float(s2):.2f}")
        