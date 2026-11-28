class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
    def __str__(self):
        return f"{self.name}: {self.phone}"
    def __repr__(self):
        return f"Contact(name={self.name!r}, phone={self.phone!r})"
name = input().strip()
phone = input().strip()
if name and phone.isdigit() and 7 <= len(phone) <= 15:
    c = Contact(name, phone)
    print(str(c))
    print(repr(c))
else:
    print("BAD")