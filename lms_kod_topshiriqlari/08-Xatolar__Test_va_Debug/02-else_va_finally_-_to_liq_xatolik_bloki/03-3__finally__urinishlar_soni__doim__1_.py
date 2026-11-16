s = input()
attempts = 0
try:
    int(s)
except ValueError:
    pass
finally:
    attempts += 1
print(attempts)