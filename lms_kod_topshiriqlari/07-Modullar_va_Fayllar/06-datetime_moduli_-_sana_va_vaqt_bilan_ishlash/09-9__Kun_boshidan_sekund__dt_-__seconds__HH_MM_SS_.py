from datetime import datetime
dt = datetime.fromisoformat(input().strip())
t = dt.time()
total = t.hour * 3600 + t.minute * 60 + t.second
print(total)