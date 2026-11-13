import json
obj = json.loads(input())
new_debug = input().strip()
obj["app"]["debug"] = (new_debug == "true")
print(json.dumps(obj, ensure_ascii=False, sort_keys=True))