def safe_div(a, b):
    if b == 0:
          return None
    return a / b
def ratio(a, b):
    natija = safe_div(a, b)
    if natija is None:
        return "ERROR"
    return f"{natija:.2f}"
a, b = map(int, input().split())
print(ratio(a, b))
