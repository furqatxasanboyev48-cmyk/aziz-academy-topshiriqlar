def lower(s):
    return s.lower()
def upper(s):
    return s.upper()
text_mod = {"lower": lower, "upper": upper}
mode = input().strip()
s = input()
print(text_mod[mode](s))
