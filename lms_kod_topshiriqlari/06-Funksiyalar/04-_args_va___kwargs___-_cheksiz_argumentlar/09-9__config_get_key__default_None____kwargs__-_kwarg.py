def config_get(key, default=None, **kwargs):
    if key in kwargs:
        return kwargs[key]
    return default
izlanayotgan = input().strip()
n = int(input())
data = {}
for i in range(n):
    qator = input().split()
    data[qator[0]] = int(qator[1])
print(config_get(izlanayotgan, default=0, **data))