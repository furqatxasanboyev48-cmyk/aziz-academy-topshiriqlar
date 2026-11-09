from datetime import date
d = date.fromisoformat(input().strip())
if d.weekday() <5:
    print("WORKDAY")
else:
    print("WEEKEND")
