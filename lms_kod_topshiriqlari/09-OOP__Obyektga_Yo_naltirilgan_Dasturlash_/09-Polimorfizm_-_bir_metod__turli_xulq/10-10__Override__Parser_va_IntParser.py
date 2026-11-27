class Parser:
    def parse(self, s):
        raise NotImplementedError
class IntParser(Parser):
    def parse(self, s):
        return int(s)
s = input().strip()
try:
    print(IntParser().parse(s))
except ValueError:
    print("BAD")