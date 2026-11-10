n = int(input())
print(max((input() for _ in range(n)), key=len))