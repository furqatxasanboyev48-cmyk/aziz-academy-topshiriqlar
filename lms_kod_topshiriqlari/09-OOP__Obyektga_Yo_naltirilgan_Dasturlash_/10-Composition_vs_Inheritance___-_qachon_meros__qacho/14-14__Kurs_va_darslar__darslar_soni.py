class Lesson:
    def __init__(self, title):
        self.title = title
class Course:
    def __init__(self):
        self.lessons = []
    def add(self, l):
        self.lessons.append(l)
    def count(self):
        return len(self.lessons)
titles = input().split()
c = Course()
for t in titles:
    c.add(Lesson(t))
print(c.count())