n = int(input())
for i in range(n):
    row = ""
    for j in range(n):
        if i == j:
            row += "*"
        else:
            row += "."
    print(row)