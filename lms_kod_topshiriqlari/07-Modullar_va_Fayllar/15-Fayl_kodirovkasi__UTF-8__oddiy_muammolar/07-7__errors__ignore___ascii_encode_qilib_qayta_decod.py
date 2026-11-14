matn = input()
baytlar = matn.encode("ascii", errors="ignore")
print(baytlar.decode("ascii"))