nums = []
def push(x):
    nums.append(x)
def last():
    if len(nums) == 0:
        return "NONE"
    return nums[-1]
q = int(input())
for i in range(q):
    qator = input().split()
    if qator[0] == 'push':
        push(int(qator[1]))
    else:
        print(last())