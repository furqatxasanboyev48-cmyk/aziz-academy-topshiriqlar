n = int(input())
d = {}
for _ in range(n):
    ism, ball = input().split()
    d[ism] = int(ball)
print(sum(d.values()))