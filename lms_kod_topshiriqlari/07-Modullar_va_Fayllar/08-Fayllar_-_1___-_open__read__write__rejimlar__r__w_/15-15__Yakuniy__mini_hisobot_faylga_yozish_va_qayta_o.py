n = int(input())
s = [int(input().split()[1])for _ in range(n)]
print(n, f"{sum(s) /n:.2f}", max(s), sep="\n")