from datetime import datetime
dt = datetime.fromisoformat(input().strip())
print(dt.strftime("%Y/%m/%d %H:%M"))