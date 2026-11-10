import time
t = int(input())
print(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(t)))