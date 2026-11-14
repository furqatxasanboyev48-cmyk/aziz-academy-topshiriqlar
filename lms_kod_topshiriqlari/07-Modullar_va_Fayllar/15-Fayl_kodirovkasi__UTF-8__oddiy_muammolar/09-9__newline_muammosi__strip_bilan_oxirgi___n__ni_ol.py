from pathlib import Path 
matn = input()
Path("enc9.txt").write_text(matn + "\n", encoding="utf-8")
oqilgan = Path("enc9.txt").read_text(encoding="utf-8")
print(oqilgan.rstrip("\n"))