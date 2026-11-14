matn = input()
with open("enc3.bin", "wb") as f:
    f.write(matn.encode("cp1251"))
try:
    with open("enc3.bin", "r", encoding="utf-8") as f:
        f.read()
    print("OK")
except UnicodeDecodeError:
    print("DECODE_ERROR")