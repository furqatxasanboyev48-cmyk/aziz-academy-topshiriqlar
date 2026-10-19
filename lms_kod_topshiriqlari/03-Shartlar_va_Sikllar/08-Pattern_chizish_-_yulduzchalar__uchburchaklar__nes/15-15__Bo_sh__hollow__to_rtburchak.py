parts = input().split()
n = int(parts[0])
m = int(parts[1])
for i in range(n):
    if i == 0 or i == n - 1:
        print("*" * m)
    else:
        print("*" + "." * (m - 2) + "*")