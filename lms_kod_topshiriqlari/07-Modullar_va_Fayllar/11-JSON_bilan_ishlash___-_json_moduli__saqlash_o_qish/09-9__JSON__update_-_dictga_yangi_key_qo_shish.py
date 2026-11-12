import json
obj = json.loads(input())
new_key = input()
new_value = input()
obj[new_key] = new_value
print(json.dumps(obj, ensure_ascii=False, sort_keys=True))