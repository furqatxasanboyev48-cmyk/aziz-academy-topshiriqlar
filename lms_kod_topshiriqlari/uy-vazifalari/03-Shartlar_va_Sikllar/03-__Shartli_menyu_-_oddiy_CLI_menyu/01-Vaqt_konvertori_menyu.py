t = input()
n = int(input())
if t == "1":
    print(f"{n // 60} minut {n % 60} soniya")
elif t == "2":
    print(f"{n // 60} soat {n % 60} minut")
else:
    print("Notogri tanlov")