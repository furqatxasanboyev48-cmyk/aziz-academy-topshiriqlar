import json
matn = input()
try:
    json.loads(matn)
    print("OK")
except json.JSONDecodeError:
    print("NO")