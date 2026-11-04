def pack_dict(**kwargs):
    return kwargs
n = int(input())
data = {}
for i in range(n):
    qator = input().split()
    data[qator[0]] = int(qator[1])
print(pack_dict(**data))