class Num:
    @staticmethod
    def is_even(n):
        return "Ha" if n % 2 == 0 else "Yo'q"
print(Num.is_even(int(input())))