def sum_named(**kwargs):
    return sum(kwargs.values())
n = int(input())
data = {}
for i in range(n):
    qator = input().split()
    data[qator[0]] = int(qator[1])
print(sum_named(**data))