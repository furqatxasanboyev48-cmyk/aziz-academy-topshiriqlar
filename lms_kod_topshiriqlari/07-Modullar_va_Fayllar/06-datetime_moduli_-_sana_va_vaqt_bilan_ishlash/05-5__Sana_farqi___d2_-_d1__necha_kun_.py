from datetime import date
d1 = date.fromisoformat(input().strip())
d2 = date.fromisoformat(input().strip())
print((d2 - d1).days)