nums = [int(x) for x in input().split()]
juft = [x for x in nums if x % 2 == 0]
if juft:
    print(" ".join(str(x) for x in juft))
else:
    print("yo'q")