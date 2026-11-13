debug = input().strip()
message = input()
with open("cfg10.txt", "w", encoding="utf-8") as f:
    f.write("debug=" + debug + "\n")
if debug == "true":
    qator = "INFO:" + message
else:
    qator = "WARN:" + message
with open("log10.txt", "w", encoding="utf-8") as f:
    f.write(qator + "\n")
with open("log10.txt", "r", encoding="utf-8") as f:
    birinchi = f.readline()
print(birinchi.split(":")[0].strip())
    