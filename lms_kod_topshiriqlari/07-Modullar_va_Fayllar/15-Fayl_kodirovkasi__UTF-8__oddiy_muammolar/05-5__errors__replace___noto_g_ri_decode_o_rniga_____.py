matn = input()
with open("enc5.bin", "wb") as f:
    f.write(matn.encode("cp1251"))
with open("enc5.bin", "rb") as f:
    baytlar = f.read()
print(baytlar.decode("utf-8", errors="replace"))