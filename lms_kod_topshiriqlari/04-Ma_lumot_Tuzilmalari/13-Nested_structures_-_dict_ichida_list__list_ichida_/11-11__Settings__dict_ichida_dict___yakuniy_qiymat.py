a = input().split()
b = input().split()
print(
     b[0] if b[0] != '-' else a[0],
     b[1] if b[1] != '-' else a[1],
     b[2] if b[2] != '-' else a[2]
)

