def my_len(s):
    return len(s)
ops = {"len": my_len}
len_fn = ops["len"]
s = input()
print(len_fn(s))