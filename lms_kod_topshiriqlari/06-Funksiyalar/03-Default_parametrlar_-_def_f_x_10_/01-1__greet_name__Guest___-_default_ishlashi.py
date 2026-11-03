def greet(name='Guest'):
    return "Hello, " + name + "!"
qator = input().strip()
if qator:
    print(greet(qator))
else:
    print(greet())
    
    