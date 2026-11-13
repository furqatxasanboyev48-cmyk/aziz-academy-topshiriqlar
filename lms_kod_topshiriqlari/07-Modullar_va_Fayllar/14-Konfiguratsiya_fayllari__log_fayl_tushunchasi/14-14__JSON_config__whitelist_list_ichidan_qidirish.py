import json
obj = json.loads(input())
item = input().strip()
if item in obj["whitelist"]:
    print("YES")
else:
    print("NO")