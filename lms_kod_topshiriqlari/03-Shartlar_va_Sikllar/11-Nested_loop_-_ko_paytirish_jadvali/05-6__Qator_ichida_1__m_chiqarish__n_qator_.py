parts = input().split()
n = int(parts[0])
if n == 0:
    print(0)
else:
    m = int(parts[1])
    for i in range(n):
        row = ""
        for j in range(1, m + 1):
            row += str(j) + " "
        print(row.strip())
    