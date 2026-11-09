from datetime import datetime, timedelta
start_dt = datetime.fromisoformat(input().strip())
ops = int(input())
elapsed_ms = int(input())
elapsed_s = elapsed_ms / 1000
finish_dt = start_dt + timedelta(milliseconds=elapsed_ms)
rate = ops / elapsed_s
start_s = start_dt.strftime("%Y-%m-%d %H:%M:%S")
finish_s = finish_dt.strftime("%Y-%m-%d %H:%M:%S")
print(f"start={start_s} finish={finish_s} rate={rate:.2f}")