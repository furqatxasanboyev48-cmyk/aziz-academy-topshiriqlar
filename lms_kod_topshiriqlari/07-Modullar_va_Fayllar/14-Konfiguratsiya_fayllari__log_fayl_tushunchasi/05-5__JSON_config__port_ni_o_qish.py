import json 
obj = json.loads(input())
with open("cfg5.json", "w", encoding="utf-8") as f:
    json.dump(obj, f, ensure_ascii=False)
with open("cfg5.json", "r", encoding="utf-8") as f:
          obj = json.load(f)
print(obj["app"]["port"])