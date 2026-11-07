def split_words(s):
    return s.split()
def longest_word(words):
    eng_uzun = words[0]
    for w in words:
        if len(w) > len(eng_uzun):
            eng_uzun = w 
    return eng_uzun
s = input()
print(longest_word(split_words(s)))