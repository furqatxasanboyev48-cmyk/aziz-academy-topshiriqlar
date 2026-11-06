s = input()
print(sum(1 for c in s.lower() if c in "aeiou"))