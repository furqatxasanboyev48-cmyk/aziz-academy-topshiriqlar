import random
seed = int(input())
a, b = map(int, input().split())
random.seed(seed)
for _ in range(5):
    print(random.randint(a, b))