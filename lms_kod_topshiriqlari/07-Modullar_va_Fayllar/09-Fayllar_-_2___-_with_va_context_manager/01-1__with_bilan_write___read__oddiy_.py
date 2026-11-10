s = input()
with open("w1.txt", "w", encoding="utf-8") as f:
    f.write(s)
with open("w1.txt", "r", encoding="utf-8") as f:
    matn = f.read()
print(matn)