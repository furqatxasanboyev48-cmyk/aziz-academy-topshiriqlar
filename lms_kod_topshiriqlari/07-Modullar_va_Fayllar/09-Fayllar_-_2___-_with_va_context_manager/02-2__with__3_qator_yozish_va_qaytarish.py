a = input()
b = input()
c = input()
with open("w2.txt", "w", encoding="utf-8") as f:
    f.write(a + "\n" + b + "\n" + c + "\n")
with open("w2.txt", "r", encoding="utf-8") as f:
    for qator in f:
        print(qator.rstrip("\n"))