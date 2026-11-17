n = int(input())
d = {}
for _ in range(n):
    k, v = input().split()
    d[k] = v 
q = input().strip()
try:
    assert q in d 
except AssertionError:
    print("NOKEY")
else:
    print("FOUND")
    