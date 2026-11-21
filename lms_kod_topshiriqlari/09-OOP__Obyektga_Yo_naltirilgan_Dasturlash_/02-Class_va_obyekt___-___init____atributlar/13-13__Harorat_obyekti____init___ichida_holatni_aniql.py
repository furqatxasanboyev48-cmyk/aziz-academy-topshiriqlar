class Harorat:
    def __init__(self, daraja):
        self.daraja = daraja
        if daraja < 10:
            self.holat = "sovuq"
        elif daraja < 25:
            self.holat = "iliq"
        else:
            self.holat = "issiq"
daraja = int(input())
h = Harorat(daraja)
print(f"{h.daraja} daraja: {h.holat}")