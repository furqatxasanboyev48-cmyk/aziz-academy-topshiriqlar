class Person:
    def __init__(self, first, last):
        self._first = first
        self._last = last
    @property
    def full_name(self):
        return f"{self._first} {self._last}"
first, last = input().split()
print(Person(first, last).full_name)
    