matn = input()
with open("enc4.bin", "wb") as f:
    f.write(matn.encode("cp1251"))
with open("enc4.bin", "rb") as f:
    baytlar = f.read()
print(baytlar.decode("cp1251"))
    