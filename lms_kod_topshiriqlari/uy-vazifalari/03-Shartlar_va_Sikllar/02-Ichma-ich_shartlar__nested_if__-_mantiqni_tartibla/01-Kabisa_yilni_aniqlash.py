yil = int(input())
if yil % 4 == 0:
    if yil % 100 == 0:
        if yil % 400 == 0:
            print("Kabisa")
        else:
            print("Kabisa emas")
    else:
        print("Kabisa")
else:
        print("Kabisa emas")
        
            