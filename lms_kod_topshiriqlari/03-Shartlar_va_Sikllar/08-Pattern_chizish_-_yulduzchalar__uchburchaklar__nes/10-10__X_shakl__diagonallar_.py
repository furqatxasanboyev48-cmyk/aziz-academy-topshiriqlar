n = int(input())
for i in range(n):
    row = ""
    for j in range(n):
        if j == i or i + j == n - 1:
            row += "*"
        else:
            row += "."
    print(row)
    