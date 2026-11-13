q1 = input()
q2 = input()
set_key = input().strip()
set_value = input().strip()
with open("cfg4.txt", "w", encoding="utf-8") as f:
    f.write(q1 + "\n" + q2 + "\n")
cfg = {}
with open("cfg4.txt", "r", encoding="utf-8") as f:
    for qator in f:
        qator = qator.rstrip("\n")
        if qator:
            k, v = qator.split("=", 1)
            cfg[k] = v 
cfg[set_key] = set_value
with open("cfg4.txt", "w", encoding="utf-8") as f:
    for k in sorted(cfg):
        f.write(k + "=" + cfg[k] + "\n")
with open("cfg4.txt", "r", encoding="utf-8") as f:
    for qator in f:
        print(qator.rstrip("\n"))
        


