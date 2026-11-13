key = input().strip()
value = input().strip()
query_key = input().strip()
with open("cfg1.txt", "w", encoding="utf-8") as f:
    f.write(key + "=" + value + "\n")
cfg = {}
with open("cfg1.txt", "r", encoding="utf-8") as f:
    for qator in f:
        qator = qator.rstrip("\n")
        if qator:
            k, v = qator.split("=", 1)
            cfg[k] = v 
    if query_key in cfg:
        print(cfg[query_key])
    else:
        print("NOTFOUND")