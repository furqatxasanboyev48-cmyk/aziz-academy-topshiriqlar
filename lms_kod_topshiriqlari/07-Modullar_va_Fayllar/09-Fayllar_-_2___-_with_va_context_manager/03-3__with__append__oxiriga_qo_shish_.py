s1 = input()
s2 = input()
with open("w3.txt", "w", encoding="utf-8") as f:
    f.write(s1)
with open("w3.txt", "a", encoding="utf-8") as f:
    f.write("\n" + s2)
with open("w3.txt", "r", encoding="utf-8") as f:
    print(f.read())
    