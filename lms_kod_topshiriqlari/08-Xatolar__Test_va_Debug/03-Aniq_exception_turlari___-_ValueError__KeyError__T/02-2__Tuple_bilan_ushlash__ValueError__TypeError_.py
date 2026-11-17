s = input().strip()
try:
    print(int(s) + 1)
except (ValueError, TypeError):
    print("ERR")