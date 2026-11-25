class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b 
a, b = map(int, input().split())
print(MathUtils.add(a, b))