n = int(input())
cfg = {}
for _ in range(n):
    k, v = input().split("=", 1)
    cfg[k] = v 
print(len(cfg))