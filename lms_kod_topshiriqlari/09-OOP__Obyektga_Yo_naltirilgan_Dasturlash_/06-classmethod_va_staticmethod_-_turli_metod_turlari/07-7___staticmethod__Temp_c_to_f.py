class Temp:
    @staticmethod
    def c_to_f(c):
        return round(c * 9 / 5 + 32, 1)
print(Temp.c_to_f(int(input())))