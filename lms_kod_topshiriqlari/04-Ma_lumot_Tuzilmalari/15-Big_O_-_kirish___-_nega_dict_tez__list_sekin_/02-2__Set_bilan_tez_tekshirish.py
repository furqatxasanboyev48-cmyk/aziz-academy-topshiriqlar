n = int(input())
s = set(int(input()) for _ in range(n))
target = int(input())
print(target in s)
