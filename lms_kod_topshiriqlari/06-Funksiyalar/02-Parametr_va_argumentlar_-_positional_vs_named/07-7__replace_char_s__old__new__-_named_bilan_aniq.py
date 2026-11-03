def replace_char(s, old, new):
    return s.replace(old, new)
s = input()
old = input()
new = input()
print(replace_char(s, old, new))
print(replace_char(new=new, s=s, old=old))