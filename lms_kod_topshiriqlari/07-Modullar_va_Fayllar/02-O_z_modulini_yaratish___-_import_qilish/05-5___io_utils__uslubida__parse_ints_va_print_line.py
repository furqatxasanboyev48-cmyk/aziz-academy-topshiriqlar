def parse_ints(line):
    return [int(x) for x in line.split()]
def print_line(items):
    return " ".join(str(x) for x in items)
nums = parse_ints(input())
ikki_barobar = [x * 2 for x in nums]
print(print_line(ikki_barobar))