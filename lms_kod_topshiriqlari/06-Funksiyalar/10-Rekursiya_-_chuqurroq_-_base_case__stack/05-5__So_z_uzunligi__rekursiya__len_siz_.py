def sl(s):
    if s == "":
        return 0
    return 1 + sl(s[1:])
print(sl(input()))