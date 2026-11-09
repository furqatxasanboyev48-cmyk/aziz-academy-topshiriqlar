from datetime import date, timedelta
d = date.fromisoformat(input().strip())
n = int(input())
new_d = d + timedelta(days=n)
print(new_d)