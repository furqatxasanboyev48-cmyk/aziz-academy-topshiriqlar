def rs(s):
    if s == "":
        return ""
    return rs(s[1:]) + s[0]
print(rs(input()))