import random
seed = int(input())
n = int(input())
random.seed(seed)
alph = "abcdefghijklmnopqrstuvwxyz"
dig = "0123456789"
pool = alph + dig
parol = ""
for _ in range(n):
    parol += random.choice(pool)
print(parol)