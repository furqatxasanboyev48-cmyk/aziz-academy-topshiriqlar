class Calc:
    @staticmethod
    def max3(a, b, c):
        return max(a,b,c)
a,b, c = map(int, input().split())
print(Calc.max3(a, b, c))