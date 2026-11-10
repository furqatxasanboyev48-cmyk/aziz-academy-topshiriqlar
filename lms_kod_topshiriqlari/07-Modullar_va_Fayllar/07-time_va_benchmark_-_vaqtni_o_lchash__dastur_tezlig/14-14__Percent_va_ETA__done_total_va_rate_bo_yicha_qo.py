done, total = map(int, input().split())
rate = float(input())
percent = done * 100 // total
remaining = total - done
eta_sec = remaining / rate
print(f"{percent}%")
print(f"{eta_sec:.2f}")