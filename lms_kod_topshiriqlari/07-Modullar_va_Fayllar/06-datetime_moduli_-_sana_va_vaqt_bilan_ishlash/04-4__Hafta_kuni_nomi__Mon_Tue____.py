from datetime import date
d = date.fromisoformat(input().strip())
names = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
print(names[d.weekday()])