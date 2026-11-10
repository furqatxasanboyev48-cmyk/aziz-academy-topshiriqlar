import time
t = int(input())
delta = int(input())
new_t = t + delta
print(time.strftime("%H:%M:%S", time.gmtime(new_t)))
