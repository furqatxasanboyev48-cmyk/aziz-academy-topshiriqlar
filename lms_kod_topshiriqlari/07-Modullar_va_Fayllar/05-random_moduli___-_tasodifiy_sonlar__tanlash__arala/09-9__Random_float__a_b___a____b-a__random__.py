import random
seed = int(input())
a, b = map(float, input().split())
random.seed(seed)
r = a + (b - a) * random.random()
print(f"{r:.4f}")