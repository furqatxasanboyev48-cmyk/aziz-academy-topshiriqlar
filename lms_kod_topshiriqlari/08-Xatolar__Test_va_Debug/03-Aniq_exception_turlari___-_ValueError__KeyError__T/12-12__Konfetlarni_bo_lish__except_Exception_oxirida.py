qutilar = input().split()
raqam = input()
try:
    i = int(raqam)
    bolalar = int(qutilar[i])
    print(60 // bolalar)
except ZeroDivisionError:
    print("DIV0")
except Exception:
    print("ERR")