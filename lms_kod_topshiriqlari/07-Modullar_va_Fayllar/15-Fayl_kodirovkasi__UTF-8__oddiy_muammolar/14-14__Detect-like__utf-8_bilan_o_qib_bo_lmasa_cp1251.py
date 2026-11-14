mode = input().strip()
text = input()
if mode == "utf8":
    with open("enc14.txt", "w", encoding="utf-8") as f:
        f.write(text)
else:
    with open("enc14.txt", "wb") as f:
        f.write(text.encode("cp1251"))
try:
    with open("enc14.txt", "r", encoding="utf-8") as f:
        print(f.read())
except UnicodeDecodeError:
    with open("enc14.txt", "r", encoding="cp1251") as f:
        print(f.read())
        
        
        
    
