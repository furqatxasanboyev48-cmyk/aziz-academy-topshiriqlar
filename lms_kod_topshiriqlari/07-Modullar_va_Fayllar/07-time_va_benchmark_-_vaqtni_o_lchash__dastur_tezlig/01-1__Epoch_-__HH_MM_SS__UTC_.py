import time
t = int(input())
tm = time.gmtime(t)
print(
f"{tm.tm_hour:02d}:{tm.tm_min:02d}:{tm.tm_sec:02d}")
