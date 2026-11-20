s = input().strip()
try:
    print(int(s) * 2)
except ValueError:
    print("BAD")
