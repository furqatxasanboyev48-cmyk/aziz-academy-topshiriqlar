from datetime import date 
d = date.fromisoformat(input().strip())
names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
print(names[d.month -1])