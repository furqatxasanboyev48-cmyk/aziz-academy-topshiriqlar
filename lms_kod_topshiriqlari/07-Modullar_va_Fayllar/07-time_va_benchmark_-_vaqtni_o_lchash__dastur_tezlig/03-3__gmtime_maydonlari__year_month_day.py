import time
t = int(input())
tm = time.gmtime(t)
print(tm.tm_year)
print(tm.tm_mon)
print(tm.tm_mday)