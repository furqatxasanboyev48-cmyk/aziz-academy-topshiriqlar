class Lock:
    def __init__(self, pin):
        self._pin = pin
    def check(self, try_pin):
        return self._pin == try_pin
def valid_pin(p):
    return len(p) == 4 and p.isdigit()
pin = input().strip()
try_pin = input().strip()
if valid_pin(pin) and valid_pin(try_pin):
    lock = Lock(pin)
    print("OK" if lock.check(try_pin) else "NO")
else:
    print("BAD")
            