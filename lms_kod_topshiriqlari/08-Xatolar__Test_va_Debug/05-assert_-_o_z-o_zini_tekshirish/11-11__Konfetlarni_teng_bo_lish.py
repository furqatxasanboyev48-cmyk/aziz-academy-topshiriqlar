n = int(input())
k = int(input())
try:
    assert k > 0, "Bolalar soni musbat bo'lishi kerak"
    print(n // k)
except AssertionError as e:
    print(e)