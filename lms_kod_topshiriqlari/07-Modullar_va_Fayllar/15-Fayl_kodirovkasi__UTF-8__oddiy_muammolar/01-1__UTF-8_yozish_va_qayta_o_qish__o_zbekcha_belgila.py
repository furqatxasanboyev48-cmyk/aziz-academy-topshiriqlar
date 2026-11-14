matn = input()
with open("enc1.txt", "w", encoding="utf-8") as f:
    f.write(matn)
with open("enc1.txt", "r", encoding="utf-8") as f:
    print(f.read())