import time
t = int(input())
tm = time.gmtime(t)
print(tm.tm_yday)