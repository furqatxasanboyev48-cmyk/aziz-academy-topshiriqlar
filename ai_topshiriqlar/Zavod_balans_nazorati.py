# Zavod: balans nazorati
# Kurs: Dasturlash / IT
# Mavzu: Dasturlashga kirish - Python nima va nega o'rganamiz
# Ball: 100
# Aziz Academy — AI Topshiriq

b = 200000
min_b = b 
chiqdim = 0
for _ in range(int(input())):
    s = input()
    x = int(s)
    b += x
    if b < min_b:
        min_b = b 
    if x < 0:
        chiqdim += 1
print(b)
print(min_b)
print(chiqdim)