from datetime import datetime
dt1 = datetime.fromisoformat(input().strip())
dt2 = datetime.fromisoformat(input().strip())
diff = (dt2 - dt1).total_seconds()
print(int(diff))