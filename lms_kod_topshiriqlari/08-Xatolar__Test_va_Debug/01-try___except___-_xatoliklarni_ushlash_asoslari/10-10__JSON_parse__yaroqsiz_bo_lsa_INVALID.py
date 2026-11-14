import json
s = input()
try:
    json.loads(s)
    print("OK")
except json.JSONDecodeError:
    print("INVALID")