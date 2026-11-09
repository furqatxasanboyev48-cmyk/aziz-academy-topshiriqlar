import random 
seed = input().strip()
n = int(input())
random.seed(seed)
inside = 0
for _ in range(n):
    x = random.random()
    y = random.random()
    if x * x + y * y <= 1:
        inside += 1
print(inside)

