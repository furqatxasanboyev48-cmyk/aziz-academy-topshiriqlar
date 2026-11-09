import random
seed = int(input())
n, a, b = map(int, input().split())
random.seed(seed)
sonlar = []
for _ in range(n):
    sonlar.append(random.randint(a, b))
print(max(sonlar))