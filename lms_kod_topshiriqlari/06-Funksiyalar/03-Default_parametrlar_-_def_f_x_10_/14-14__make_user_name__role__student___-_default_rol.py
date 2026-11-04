def make_user(name, role='student'):
    return f"name={name}, role={role}"
qator = input().split()
if len(qator) == 1:
    print(make_user(qator[0]))
else:
    print(make_user(qator[0], qator[1]))