ops,elapsed_ms = map(int, input().split())
rate = ops / (elapsed_ms / 1000)
print(f"ops={ops} time={elapsed_ms}ms rate={rate:.2f}")