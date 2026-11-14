s = input().strip()
try:
    x = float(s)
except ValueError:
    x = 0.0
print(f"{x:.2f}")
    