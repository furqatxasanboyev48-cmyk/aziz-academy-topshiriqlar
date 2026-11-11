matn = input()
with open("w5.txt", "w", encoding="utf-8") as f:
    f.write(matn)
with open("w5.txt", "r", encoding="utf-8") as f:
    kontent = f.read()
print(len(kontent.split()))