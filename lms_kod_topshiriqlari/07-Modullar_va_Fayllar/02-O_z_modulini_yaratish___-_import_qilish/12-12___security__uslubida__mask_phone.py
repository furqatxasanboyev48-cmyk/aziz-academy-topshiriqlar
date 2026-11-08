def mask_phone(s):
    raqamlar = ""
    for ch in s:
        if ch.isdigit():
            raqamlar += ch 
    raqamlar = raqamlar[-11:]
    if len(raqamlar) < 4 :
        return "*" * len(raqamlar)
    return "*" * (len(raqamlar) - 4) + raqamlar[-4:]
s = input()
print(mask_phone(s))