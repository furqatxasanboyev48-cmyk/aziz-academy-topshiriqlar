# Bitta qatorda ism va n kiriting: masalan "Aziz 3".
# Ismni n marta ketma-ket bo'shliq bilan chiqarib bering.
# Masalan: "Aziz 2" -> "Aziz Aziz"
ism, n = input().split()
n = int(n)
print(((ism + " ") * n).strip())