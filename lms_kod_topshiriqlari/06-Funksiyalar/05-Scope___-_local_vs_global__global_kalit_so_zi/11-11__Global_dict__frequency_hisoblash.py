freq = {}
def add_word(w):
    w = w.lower()
    if w in freq:
        freq[w] += 1
    else:
        freq[w] = 1
n = int(input())
for i in range(n):
    add_word(input().strip())
for k in sorted(freq.keys()):
    print(k, freq[k])
        