parts = input().split()
n = int(parts[0])
m = int(parts[1])
for i in range(1, n + 1):
    row = ""
    for j in range(m):
        row += str(i) + " "
    print(row.strip())
