from datetime import datetime, timedelta
dt = datetime.fromisoformat(input().strip())
h, m, s = map(int, input().split())
delta = timedelta(hours=h, minutes=m, seconds=s)
new_dt = dt + delta
print(new_dt.strftime("%Y-%m-%d %H:%M:%S"))