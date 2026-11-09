import random
seed = int(input())
random.seed(seed)
d1 = random.randint(1, 6)
d2 = random.randint(1, 6)
print(d1)
print(d2)
print(d1 + d2)