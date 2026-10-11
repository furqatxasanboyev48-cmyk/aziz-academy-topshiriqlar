parts = input().split()
a = int(parts[0])
b = int(parts[1])
c = int(parts[2])
if a == b:
    if b == c:
        print("All equal")
    else:
        print("Partially equal")
else:
    print("Not equal")