class Safe:
    def __init__(self, pin):
        self.__pin = pin
    def verify(self, try_pin):
        return self.__pin == try_pin
def valid_pin(p):
    return len(p) == 4 and p.isdigit()
pin = input().strip()
try_pin = input().strip()
if valid_pin(pin) and valid_pin(try_pin):
    safe = Safe(pin)
    print("OK" if safe.verify(try_pin) else "NO")
else:
    print("BAD")
        
    