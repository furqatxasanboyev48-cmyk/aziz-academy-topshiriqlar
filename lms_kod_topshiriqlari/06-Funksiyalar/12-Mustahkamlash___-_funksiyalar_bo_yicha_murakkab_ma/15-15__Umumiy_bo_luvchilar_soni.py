a, b = map(int, input().split())
print(sum(1 for d in range(1, min(a, b) + 1) if a % d == 0 and b % d == 0))