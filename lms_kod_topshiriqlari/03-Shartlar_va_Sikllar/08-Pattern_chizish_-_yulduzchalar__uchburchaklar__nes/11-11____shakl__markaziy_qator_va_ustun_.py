n = int(input())
c = n // 2
for i in range(n):
    row = ""
    for j in range(n):
        if i == c or j == c:
            row += "*"
        else:
            row += "."
    print(row)
            
            
        