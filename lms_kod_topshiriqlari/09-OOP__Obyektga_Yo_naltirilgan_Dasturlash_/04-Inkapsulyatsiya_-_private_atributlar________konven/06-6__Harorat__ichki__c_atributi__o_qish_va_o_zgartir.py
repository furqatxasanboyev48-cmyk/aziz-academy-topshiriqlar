class Temperature:
    def __init__(self, c):
        self._c = c 
    @property
    def celsius(self):
        return self._c
    @celsius.setter
    def celsius(self, value):
        self._c = value
try:
    c = int(input().strip())
    new_c = int(input().strip())
except ValueError:
    print("BAD")
else:
    t = Temperature(c)
    t.celsius = new_c
    print(f"C={t.celsius}")
    

    
        