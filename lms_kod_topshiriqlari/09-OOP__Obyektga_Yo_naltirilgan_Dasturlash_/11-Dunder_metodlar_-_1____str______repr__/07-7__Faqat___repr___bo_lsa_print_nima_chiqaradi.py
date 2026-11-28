class Tag:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f"Tag('{self.name}')"
name = input().strip()
if name:
    print(Tag(name))
else:
    print("BAD")