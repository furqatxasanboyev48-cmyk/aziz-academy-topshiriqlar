def format_point(x, y):
    return f"({x},{y})"
qator = input().split()
x = int(qator[0])
y = int(qator[1])
print(format_point(x,y))
print(format_point(y=y,x=x))