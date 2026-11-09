import random
seed = int(input())
random.seed(seed)
sonlar = []
for _ in range(6):
    sonlar.append(random.randint(1, 49))
sonlar.sort()
print(" ".join(str(x) for x in sonlar))