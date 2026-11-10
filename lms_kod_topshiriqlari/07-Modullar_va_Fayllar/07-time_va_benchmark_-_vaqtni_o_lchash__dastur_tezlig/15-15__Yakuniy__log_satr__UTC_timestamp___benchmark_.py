import time
t = int(input())
ops = int(input())
elapsed_ms = int(input())
ts = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(t))
rate = ops / (elapsed_ms / 1000)
print(f"[{ts}] ops={ops} time={elapsed_ms}ms rate={rate:.2f}")