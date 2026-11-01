sonlar =[int(x) for x in input().split()]
unik = {x for x in sonlar}
natija = [str(x) for x in sorted(unik)]
print(" ".join(natija))
             
