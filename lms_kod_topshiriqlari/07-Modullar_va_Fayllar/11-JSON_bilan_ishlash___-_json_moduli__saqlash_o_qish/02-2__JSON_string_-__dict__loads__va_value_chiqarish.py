import json
obj = json.loads(input())
qiymatlar = []
for key in sorted(obj.keys()):
    qiymatlar.append(str(obj[key]))
print(" ".join(qiymatlar))