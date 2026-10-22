n = int(input())
for i in range(n):
    row = ""
    for j in range(n):
        if i == j or i + j == n - 1:
            row += "*"
        else:
            row += "."
    print(row)