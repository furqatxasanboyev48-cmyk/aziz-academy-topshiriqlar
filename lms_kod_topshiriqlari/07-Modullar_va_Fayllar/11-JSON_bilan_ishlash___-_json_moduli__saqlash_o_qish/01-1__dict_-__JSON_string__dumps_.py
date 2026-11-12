import json
key = input()
value = input()
d = {key: value}
print(json.dumps(d, ensure_ascii=False,sort_keys=True))