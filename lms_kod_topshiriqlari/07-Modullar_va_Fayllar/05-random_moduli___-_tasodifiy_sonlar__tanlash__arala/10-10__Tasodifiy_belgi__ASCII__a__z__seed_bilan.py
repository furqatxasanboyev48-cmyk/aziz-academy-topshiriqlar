import random
seed = int(input())
random.seed(seed)
harf = chr(random.randint(ord("a"), ord("z")))
print(harf)