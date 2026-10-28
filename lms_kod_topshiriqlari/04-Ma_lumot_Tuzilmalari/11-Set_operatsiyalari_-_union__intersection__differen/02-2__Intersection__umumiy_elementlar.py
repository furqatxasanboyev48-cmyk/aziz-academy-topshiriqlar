a = set(map(int, input().split()))
b = set(map(int, input().split()))
kesishma = a & b
if kesishma:
    print(" ".join(str(x) for x in sorted(kesishma)))
else:
    print("BO'SH")