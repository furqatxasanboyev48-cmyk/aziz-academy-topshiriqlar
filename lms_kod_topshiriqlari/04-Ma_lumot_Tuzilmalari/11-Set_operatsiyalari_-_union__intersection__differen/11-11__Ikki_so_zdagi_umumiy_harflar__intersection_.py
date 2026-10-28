a = input().strip()
b = input().strip()
umumiy = set(a) & set(b)
if umumiy:
    print("".join(sorted(umumiy)))
else:
    print("BO'SH")