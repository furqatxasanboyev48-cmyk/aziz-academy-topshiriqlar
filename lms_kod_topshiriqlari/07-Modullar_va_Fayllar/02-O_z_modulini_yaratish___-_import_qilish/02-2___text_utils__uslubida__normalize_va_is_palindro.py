def normalize(s):
    toza = ""
    for ch in s.lower():
        if ch.isalpha():
            toza += ch 
    return toza
def is_palindrome(s):
    t = normalize(s)
    return t == t[::-1]
s = input()
print(is_palindrome(s))
        
    