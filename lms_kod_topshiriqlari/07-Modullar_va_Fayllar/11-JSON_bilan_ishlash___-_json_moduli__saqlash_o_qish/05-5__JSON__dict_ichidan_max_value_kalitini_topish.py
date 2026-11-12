import json
obj = json.loads(input())
best = None
for key in sorted(obj.keys()):
    if best is None or obj[key] > obj[best]:
        best = key 
print(best)