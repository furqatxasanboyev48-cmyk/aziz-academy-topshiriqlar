n = int(input())
d = {}
for _ in range(n):
    k, v = input().split()
    d[k] = v 
q = input().strip()
try:
    print(int(d[q]))
except KeyError:
    print("NOKEY")
except ValueError:
    print("BADVAL")
    