words = input().split()
print(' '.join(sorted(words, key=len)))