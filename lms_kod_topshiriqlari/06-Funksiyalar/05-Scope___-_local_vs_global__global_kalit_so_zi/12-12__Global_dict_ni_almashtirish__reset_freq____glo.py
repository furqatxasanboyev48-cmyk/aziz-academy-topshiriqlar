freq = {'a': 1}
def reset_freq():
    global freq
    freq = {}
def add_word(w):
    w = w.lower()
    if w in freq:
        freq[w] += 1
    else:
        freq[w] = 1
word = input().strip()
reset_freq()
add_word(word)
print(freq)