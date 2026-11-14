text_utf = input()
text_ru = input()
with open("enc13_a.txt", "w", encoding="utf-8") as f:
    f.write(text_utf)
with open("enc13_b.bin", "wb") as f:
    f.write(text_ru.encode("cp1251"))
with open("enc13_a.txt", "r", encoding="utf-8") as f:
    print(f.read())
with open("enc13_b.bin", "rb") as f:
    print(f.read().decode("cp1251"))
