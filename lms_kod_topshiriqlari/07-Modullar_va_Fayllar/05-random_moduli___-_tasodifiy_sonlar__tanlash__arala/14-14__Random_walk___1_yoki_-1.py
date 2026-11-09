import random
seed = int(input())
n = int(input())
random.seed(seed)
pos = 0
for _ in range(n):
    if random.random() < 0.5:
        pos += 1
    else:
        pos -=1
print(pos)
    