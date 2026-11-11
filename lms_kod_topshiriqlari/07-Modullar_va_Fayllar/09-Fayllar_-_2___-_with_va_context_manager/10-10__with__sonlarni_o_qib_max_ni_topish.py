n = int(input())
sonlar = []
for _ in range(n):
    sonlar.append(input())
with open("w10.txt", "w", encoding="utf-8") as f:
    for s in sonlar:
        f.write(s + "\n")
with open("w10.txt", "r", encoding="utf-8") as f:
    eng_katta = None
    for qator in f:
        son = int(qator.strip())
        if eng_katta is None or son > eng_katta:
            eng_katta = son 
print(eng_katta)
        
        