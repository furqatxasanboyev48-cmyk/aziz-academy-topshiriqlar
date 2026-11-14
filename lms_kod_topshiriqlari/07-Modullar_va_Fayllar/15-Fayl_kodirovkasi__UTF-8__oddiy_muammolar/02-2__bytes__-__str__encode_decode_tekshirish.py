matn = input()
baytlar = matn.encode("utf-8")
qayta = baytlar.decode("utf-8")
if qayta == matn:
    print("YES")
else:
    print("NO")