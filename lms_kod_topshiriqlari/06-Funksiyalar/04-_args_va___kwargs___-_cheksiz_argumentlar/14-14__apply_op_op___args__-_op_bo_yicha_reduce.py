def apply_op(op, *args):
    if op == 'sum':
        return sum(args)
    natija = 1
    for x in args:
        natija *= x
    return natija 
op = input().strip()
nums = [int(t) for t in input().split()]
print(apply_op(op, *nums))

        