from datetime import date 
a1, a2 = input().split()
b1, b2 = input().split()
a1 = date.fromisoformat(a1)
a2 = date.fromisoformat(a2)
b1 = date.fromisoformat(b1)
b2 = date.fromisoformat(b2)
if max(a1, b1) <= min(a2, b2):
    print("YES")
else:
    print("NO")