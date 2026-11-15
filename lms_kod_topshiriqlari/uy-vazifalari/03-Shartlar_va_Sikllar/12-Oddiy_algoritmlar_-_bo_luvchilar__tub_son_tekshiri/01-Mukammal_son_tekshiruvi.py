n = int(input())
total = 0
for i in range(1, n):
    if n % i == 0:
        total += i
if total == n:
    print("MUKAMMAL")
else:
    print("MUKAMMAL EMAS")
    