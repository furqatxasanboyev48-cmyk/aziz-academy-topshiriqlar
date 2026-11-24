class Student:
    def __init__(self, a, b, c):
        self._a, self._b, self._c = a, b, c 
    @property
    def average(self):
        return(self._a + self._b + self._c) // 3
a, b, c = map(int, input().split())
print(Student(a, b, c).average)
        