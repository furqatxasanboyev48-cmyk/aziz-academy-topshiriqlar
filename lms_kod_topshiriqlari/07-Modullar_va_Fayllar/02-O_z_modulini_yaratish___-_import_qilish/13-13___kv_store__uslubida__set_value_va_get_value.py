store = {}
def set_value(key, val):
    store[key] = val 
def get_value(key, default=None):
    if key in store:
        return store[key]
    return default
q = int(input())
for _ in range(q):
    qism = input().split()
    if qism[0] == "set":
        set_value(qism[1], qism[2])
    else:
        natija = get_value(qism[1])
        if natija is None:
            print("NONE")
        else:
            print(natija)