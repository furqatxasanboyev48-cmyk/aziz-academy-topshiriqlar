class Exam:
    def __init__(self):
        self._score = 0
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self, v):
        if v < 0:
            v = 0
        elif v > 100:
            v = 100
        self._score = v 
e = Exam()
e.score = int(input())
print(e.score)