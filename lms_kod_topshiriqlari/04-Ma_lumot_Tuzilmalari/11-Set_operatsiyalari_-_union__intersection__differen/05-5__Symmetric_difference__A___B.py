a = set(map(int, input().split()))
b = set(map(int, input().split()))
simmetrik = a ^ b
if simmetrik:
    print(" ".join(str(x) for x in sorted(simmetrik)))
else:
    print("BO'SH")