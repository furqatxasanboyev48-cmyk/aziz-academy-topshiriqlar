def pick(**kwargs):
    natija = {}
    for k, v in kwargs.items():
        if v > 0:
            natija[k] = v 
    return natija
n = int(input())
data = {}
for i in range(n):
    qator = input().split()
    data[qator[0]] = int(qator[1])
print(pick(**data))