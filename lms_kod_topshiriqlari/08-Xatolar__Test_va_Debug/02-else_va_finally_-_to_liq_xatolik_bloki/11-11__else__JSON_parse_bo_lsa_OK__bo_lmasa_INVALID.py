import json
s = input()
try:
    json.loads(s)
except json.JSONDecodeError:
    print("INVALID")
else:
    print("OK")