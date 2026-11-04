def describe(*args, **kwargs):
    return {
        'args_count': len(args),
        'args_sum': sum(args),
        'kwargs_count': len(kwargs),
        'kwargs_sum': sum(kwargs.values())
    }
    
nums = [int(t) for t in input().split()]
n = int(input())
data = {}
for i in range(n):
    qator = input().split()
    data[qator[0]] = int(qator[1])
    
print(describe(*nums, **data))
    