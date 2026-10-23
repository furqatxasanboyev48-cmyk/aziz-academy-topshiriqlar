c = 0
while True:
    line = input()
    if line.strip() == "0":
        break
    parts = line.split()
    a = int(parts[0])
    b = int(parts[1])
    tanlov = int(input())
    c += 1
print(c)