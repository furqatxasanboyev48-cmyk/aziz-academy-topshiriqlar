matn = input()
with open("enc10.txt", "wb") as f:
    f.write(("\ufeff" + matn).encode("utf-8"))
with open("enc10.txt", "r", encoding="utf-8-sig") as f:
    print(f.read())