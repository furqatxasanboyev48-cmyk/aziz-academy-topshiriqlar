def rename_keys(prefix='', **kwargs):
    natija = {}
    for k, v in kwargs.items():
        natija[prefix + k] = v 
    return natija 
pref = input()
n = int(input())
data = {}
for i in range(n):
    qator = input().split()
    data[qator[0]] = int(qator[1])
print(rename_keys(pref, ** data))
