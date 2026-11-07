def count_vowels(s):
    son = 0
    for ch in s.lower():
        if ch in "aeiou":
            son += 1
    return son 
def count_consonants(s):
    son = 0
    for ch in s.lower():
        if ch.isalpha() and ch not in "aeiou":
            son += 1
    return son
s = input()
print(count_vowels(s))
print(count_consonants(s))
    