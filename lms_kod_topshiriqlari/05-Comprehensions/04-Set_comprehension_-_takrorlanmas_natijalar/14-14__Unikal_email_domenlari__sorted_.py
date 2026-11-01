emaillar = input().split()
domenlar = {e.split("@")[1].lower() for e in emaillar}
if domenlar:
    print(" ".join(sorted(domenlar)))
else:
    print("BO'SH")