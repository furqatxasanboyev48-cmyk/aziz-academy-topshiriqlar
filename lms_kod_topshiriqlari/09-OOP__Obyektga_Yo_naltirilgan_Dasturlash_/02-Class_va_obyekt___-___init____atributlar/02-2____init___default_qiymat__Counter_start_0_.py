class Counter:
    def __init__(self, start=0):
        self.value = start 
mode = input().strip()
if mode == "DEF":
    print(Counter().value)
elif mode == "CUSTOM":
    try:
        start = int(input().strip())
    except ValueError:
        print("BAD")
    else:
        print(Counter(start).value)
else:
    print("BAD")
    