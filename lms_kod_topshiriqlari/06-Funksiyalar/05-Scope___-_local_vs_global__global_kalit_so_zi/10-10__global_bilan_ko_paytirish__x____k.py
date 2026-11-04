x = 2 
def mul_global(k):
    global x 
    x *= k 
    return x 
n = int(input())
for i in range(n):
    k = int(input())
    print(mul_global(k))
    