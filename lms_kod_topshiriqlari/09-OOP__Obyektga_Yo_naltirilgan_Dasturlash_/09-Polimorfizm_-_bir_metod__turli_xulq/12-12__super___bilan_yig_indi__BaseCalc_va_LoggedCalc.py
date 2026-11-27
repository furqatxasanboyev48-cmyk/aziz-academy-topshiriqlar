class BaseCalc:
    def add(self, a, b):
        return a + b 
class LoggedCalc(BaseCalc):
    def add(self, a, b):
        result = super().add(a, b)
        print(f"SUM={result}")
        return result
try:
    a = int(input().strip())
    b = int(input().strip())
except ValueError:
    print("BAD")
else:
    LoggedCalc().add(a, b)
    