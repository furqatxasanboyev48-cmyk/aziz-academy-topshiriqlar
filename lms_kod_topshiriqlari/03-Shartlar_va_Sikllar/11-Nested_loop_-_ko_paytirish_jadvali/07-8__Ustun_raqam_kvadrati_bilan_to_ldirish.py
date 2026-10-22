parts = input().split()
n = int(parts[0])
m = int(parts[1])
row = ""
for j in range(n, m + 1):
    row += str(j * j) + " "
print(row.strip())