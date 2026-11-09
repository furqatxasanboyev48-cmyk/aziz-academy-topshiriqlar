from datetime import date 
s = input().strip()
try:
    date.fromisoformat(s)
    print("OK")
except ValueError:
    print("NO")