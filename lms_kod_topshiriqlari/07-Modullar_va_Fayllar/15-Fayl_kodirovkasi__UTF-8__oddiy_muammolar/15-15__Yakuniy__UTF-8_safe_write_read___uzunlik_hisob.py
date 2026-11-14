matn = input()
with open("enc15.txt", "w", encoding="utf-8") as f:
    f.write(matn)
with open("enc15.txt", "r", encoding="utf-8") as f:
    oqilgan = f.read()
print(len(oqilgan))