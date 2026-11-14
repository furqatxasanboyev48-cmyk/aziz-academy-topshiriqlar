import json
word = input()
obj = {"word": word}
with open("enc11.json", "w", encoding="utf-8") as f:
    json.dump(obj, f, ensure_ascii=False)
with open("enc11.json", "r", encoding="utf-8") as f:
    qayta = json.load(f)
print(qayta["word"])    