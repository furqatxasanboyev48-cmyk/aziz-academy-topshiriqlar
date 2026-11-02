amal = input()
balans = int(input())
summa = int(input())
if amal == "1":
    print(balans)
elif amal == "2":
    if summa <= balans:
        print(balans - summa)
    else:
        print("Mablag' yetarli emas")
elif amal == "3":
    print(balans + summa)
else:
    print("Notogri amal")
        