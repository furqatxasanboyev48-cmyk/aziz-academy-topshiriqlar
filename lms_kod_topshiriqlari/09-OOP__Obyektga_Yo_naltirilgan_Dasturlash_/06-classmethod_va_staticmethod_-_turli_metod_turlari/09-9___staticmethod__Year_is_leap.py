class Year:
    @staticmethod
    def is_leap(y):
        return "Ha" if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0 else "Yo'q"
print(Year.is_leap(int(input())))