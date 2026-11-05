def vc(s):
    if s == "":
        return 0 
    return (1 if s[0].lower() in "aeiou" else 0) + vc(s[1:])
print(vc(input()))