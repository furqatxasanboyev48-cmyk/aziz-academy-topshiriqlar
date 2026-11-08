def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
            return False
def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
s = input()
print(is_int(s))
print(is_float(s))
        