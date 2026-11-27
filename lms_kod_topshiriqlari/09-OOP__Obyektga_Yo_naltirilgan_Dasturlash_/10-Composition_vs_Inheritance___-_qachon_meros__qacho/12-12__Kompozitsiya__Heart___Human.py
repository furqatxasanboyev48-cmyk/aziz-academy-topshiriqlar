class Heart:
    def __init__(self, bpm):
        self.bpm = bpm
class Human:
    def __init__(self, bpm):
        self.heart = Heart(bpm)
    def alive(self):
        return "Tirik" if self.heart.bpm > 0 else "O'lik"
print(Human(int(input())).alive())    