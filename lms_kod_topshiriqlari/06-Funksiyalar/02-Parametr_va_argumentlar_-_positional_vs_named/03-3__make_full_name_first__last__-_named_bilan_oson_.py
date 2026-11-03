def make_full_name(first, last):
    return first + " " + last
first = input().strip()
last = input().strip()
print(make_full_name(first, last))
print(make_full_name(last=last, first=first))