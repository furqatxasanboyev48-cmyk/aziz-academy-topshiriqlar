counter = 0
def inc():
    global counter
    counter += 1
    return counter
def reset():
    global counter
    counter = 0
    return 0
q = int(input())
for i in range(q):
    buyruq = input().strip()
    if buyruq == 'inc':
        print(inc())
    else:
        print(reset())
    