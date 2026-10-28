ids = set(map(int, input().split()))
banned = set(map(int, input().split()))
_ = input()  
ruxsat = ids - banned
if ruxsat:
    print(" ".join(str(x) for x in sorted(ruxsat)))
else:
    print("BO'SH")