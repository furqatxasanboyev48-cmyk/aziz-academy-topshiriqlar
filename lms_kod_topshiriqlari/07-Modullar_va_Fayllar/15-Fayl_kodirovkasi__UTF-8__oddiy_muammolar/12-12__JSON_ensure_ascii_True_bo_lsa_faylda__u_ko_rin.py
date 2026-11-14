import json
word = input()
obj = {"word": word}
with open("enc12.json", "w", encoding="utf-8") as f:
    json.dump(obj, f, ensure_ascii=True)
with open("enc12.json", "r", encoding="utf-8") as f:
    matn = f.read()
if "\\u" in matn:
    print("YES")
else:
    print("NO")