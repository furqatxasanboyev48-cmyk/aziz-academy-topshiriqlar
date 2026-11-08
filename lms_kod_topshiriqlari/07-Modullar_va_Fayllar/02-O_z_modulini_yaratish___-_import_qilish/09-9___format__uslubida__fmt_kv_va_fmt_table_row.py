def fmt_kv(key, value):
    return key + "=" + value
def fmt_table_row(a, b, c):
    return a + " | " + b + " | " + c
key = input()
value = input()
a, b, c = input().split()
print(fmt_kv(key, value))
print(fmt_table_row(a, b, c))
    