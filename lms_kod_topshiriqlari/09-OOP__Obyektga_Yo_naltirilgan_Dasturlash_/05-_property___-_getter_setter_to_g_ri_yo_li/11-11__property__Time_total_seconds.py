class Time:
    def __init__(self, m, s):
        self._m = m 
        self._s = s
    @property
    def total_seconds(self):
        return self._m * 60 + self._s
m, s = map(int, input().split())
print(Time(m, s).total_seconds)