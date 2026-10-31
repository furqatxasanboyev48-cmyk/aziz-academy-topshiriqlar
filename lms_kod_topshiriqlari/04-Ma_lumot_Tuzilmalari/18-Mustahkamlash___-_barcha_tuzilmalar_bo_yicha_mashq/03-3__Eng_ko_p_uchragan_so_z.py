words = input().split()
cnt = {}
for w in words:
    cnt[w] = cnt.get(w, 0) + 1
print(max(cnt, key = cnt.get))