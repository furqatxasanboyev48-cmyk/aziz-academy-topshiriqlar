matn = input()
try:
    matn.encode("ascii")
    print("OK")
except UnicodeEncodeError:
    print("ENCODE_ERROR")