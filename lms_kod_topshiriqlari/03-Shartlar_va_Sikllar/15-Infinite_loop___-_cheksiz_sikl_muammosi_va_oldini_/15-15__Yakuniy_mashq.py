s = input()
if s.isdigit():
    n = int(s)
    parts = input().split()
    lst = []
    for p in parts:
        lst.append(int(p))
    print(lst[0])
    print(lst[1:-1])
    print(lst[-1])
else:
    line = s
    while True:
        if line == "stop":
            break
        print("Working")
        line = input()
    
    