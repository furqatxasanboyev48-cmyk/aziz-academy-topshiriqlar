n = int(input())
a = list(map(int, input().split()))
b = a[:]
b[0] = 99
print(a)
print(b)