k = int(input())
config = {}
for _ in range(k):
    kalit, qiymat = input().split()
    config[kalit] = int(qiymat)
q = int(input())
for _ in range(q):
    kalit = input().strip()
    print(config.get(kalit, 0))