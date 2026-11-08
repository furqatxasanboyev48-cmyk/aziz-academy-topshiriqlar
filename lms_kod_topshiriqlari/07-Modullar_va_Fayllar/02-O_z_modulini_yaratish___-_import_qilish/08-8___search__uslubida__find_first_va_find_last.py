def find_first(s, ch):
    return s.find(ch)
def find_last(s, ch):
    return s.rfind(ch)
s = input()
ch = input()
print(find_first(s, ch))
print(find_last(s, ch))