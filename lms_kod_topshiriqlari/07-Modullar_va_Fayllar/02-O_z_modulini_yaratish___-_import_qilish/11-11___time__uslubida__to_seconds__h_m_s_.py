def to_seconds(h, m, s):
    return h * 3600 + m * 60 + s 
def to_hms(total):
    h = total // 3600
    m = (total % 3600) // 60
    s = total % 60
    return (h, m, s)
h, m, s = map(int, input().split())
total = to_seconds(h, m, s)
print(total)
h2, m2, s2 = to_hms(total)
print(h2, m2, s2)
    