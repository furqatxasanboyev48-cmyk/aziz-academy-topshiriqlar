q1 = input()
q2 = input()
query_key = input().strip()
with open("cfg12.txt", "w", encoding="utf-8") as f:
    f.write(q1 + "\n" + q2 + "\n")
cfg = {}
with open("cfg12.txt", "r", encoding="utf-8") as f:
    for qator in f:
        qator = qator.rstrip("\n")
        if qator:
            k, v = qator.split("=", 1)
            cfg[k] = v 
if query_key in cfg:
    print(cfg[query_key])
else:
    print("NOTFOUND")
    