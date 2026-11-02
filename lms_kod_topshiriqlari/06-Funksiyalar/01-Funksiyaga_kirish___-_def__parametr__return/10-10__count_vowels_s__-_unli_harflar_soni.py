def count_vowels(s):
    soni = 0
    for harf in s.lower():
        if harf in "aeiou":
            soni += 1
    return soni
s = input()
print(count_vowels(s))