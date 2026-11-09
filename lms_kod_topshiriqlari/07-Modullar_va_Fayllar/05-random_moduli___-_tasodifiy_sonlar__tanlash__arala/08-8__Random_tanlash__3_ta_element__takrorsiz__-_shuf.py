import random
seed = int(input())
items = input().split()
random.seed(seed)
random.shuffle(items)
tanlangan = items[:3]
print(" ".join(tanlangan))