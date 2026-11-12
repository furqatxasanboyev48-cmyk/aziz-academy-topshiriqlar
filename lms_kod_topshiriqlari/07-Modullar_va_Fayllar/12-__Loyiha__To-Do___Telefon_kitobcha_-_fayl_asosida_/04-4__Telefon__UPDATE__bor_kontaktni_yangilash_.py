name, phone = input().split()
up_name, new_phone = input().split()
query_name = input().strip()
with open("pbook4.txt", "w", encoding="utf-8") as f:
    f.write(name + "=" + phone + "\n")
kitob = {}
with open("pbook4.txt", "r", encoding="utf-8") as f:
    for qator in f:
        qator = qator.rstrip("\n")
        if qator:
            k, v = qator.split("=", 1)
            kitob[k] = v 
kitob[up_name] = new_phone
with open("pbook4.txt", "w", encoding="utf-8") as f:
    for k, v in kitob.items():
        f.write(k + "=" + v + "\n")
if query_name in kitob:
    print(kitob[query_name])
else:
    print("NOTFOUND")
            
    