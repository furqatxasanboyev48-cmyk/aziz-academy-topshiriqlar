import random
seed = int(input())
random.seed(seed)
for _ in range(3):
    print(f"{random.random():.6f}")