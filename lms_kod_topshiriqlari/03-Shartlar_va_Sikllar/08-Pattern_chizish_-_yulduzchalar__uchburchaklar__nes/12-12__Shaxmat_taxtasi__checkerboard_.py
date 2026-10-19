parts = input().split()
n = int(parts[0])
m = int(parts[1])
for i in range(n):
    row = ""
    for j in range(m):
        if (i + j) % 2 == 0:
            row += "*"
        else:
            row += "."
    print(row)