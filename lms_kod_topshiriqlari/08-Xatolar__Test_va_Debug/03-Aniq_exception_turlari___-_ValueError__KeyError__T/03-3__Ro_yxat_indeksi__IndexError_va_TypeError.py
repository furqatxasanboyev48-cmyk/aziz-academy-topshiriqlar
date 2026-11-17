n = int(input())
lst = [input() for _ in range(n)]
raw = input().strip()
try:
    idx = int(raw)
except ValueError:
    idx = raw
try:
    print(lst[idx])
except IndexError:
    print("OUT")
except TypeError:
    print("TYPE")
    
    