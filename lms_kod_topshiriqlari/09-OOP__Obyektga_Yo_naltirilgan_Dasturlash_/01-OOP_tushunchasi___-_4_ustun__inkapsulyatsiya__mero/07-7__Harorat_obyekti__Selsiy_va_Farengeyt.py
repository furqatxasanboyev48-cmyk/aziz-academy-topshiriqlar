class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius
    def get_c(self):
        return int(round(self._celsius))
    def get_f(self):
        return int(round(self._celsius * 9 / 5 + 32))
scale = input().strip()
try:
    value = int(input().strip())
except ValueError:
    print("BAD")
else:
    if scale == "C":
        t = Temperature(value)
    elif scale == "F":
        t = Temperature((value - 32) * 5 / 9)
    else:
        t = None 
    if t is None:
        print("BAD")
    else:
        print(f"C={t.get_c()}")
        print(f"F={t.get_f()}")