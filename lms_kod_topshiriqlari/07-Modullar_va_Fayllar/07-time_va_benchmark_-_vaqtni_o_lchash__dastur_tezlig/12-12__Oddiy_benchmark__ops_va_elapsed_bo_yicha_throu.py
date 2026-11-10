ops = int(input())
elapsed_ms = int(input())
elapsed_s = elapsed_ms / 1000
rate = ops / elapsed_s
print(f"{rate:.2f}")

