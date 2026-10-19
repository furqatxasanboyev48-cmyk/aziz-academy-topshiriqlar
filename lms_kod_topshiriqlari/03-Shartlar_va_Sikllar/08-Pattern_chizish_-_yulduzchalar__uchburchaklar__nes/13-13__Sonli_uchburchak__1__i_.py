n =int(input())
for i in range(1, n + 1):
    row = ""
    for j in range(1, i + 1):
        row += str(j)
    print(row)
    