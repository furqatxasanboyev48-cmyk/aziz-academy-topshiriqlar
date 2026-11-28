class Library:
    def __init__(self, titles):
        self.titles = titles 
    def __len__(self):
        return len(self.titles)
    def __eq__(self, other):
        return self.titles == other.titles
    def __lt__(self, other):
        return len(self) < len(other)
def read_titles(n):
    titles = []
    for _ in range(n):
        title = input().strip()
        if not title:
            raise ValueError
        titles.append(title)
    return titles
try:
    n = int(input().strip())
    if n < 0:
        raise ValueError
    lib1 = Library(read_titles(n))    
    m = int(input().strip())
    if m < 0:
        raise ValueError
    lib2 = Library(read_titles(m))
    print(f"LEN1={len(lib1)} LEN2={len(lib2)}")
    print("EQ" if lib1 == lib2 else "NEQ")
    print("LT" if lib1 < lib2 else "GE")
except ValueError:
    print("BAD")