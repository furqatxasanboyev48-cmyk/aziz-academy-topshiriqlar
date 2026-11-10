import time
t = int(input())
tm = time.gmtime(t)
names = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
print(names[tm.tm_wday])