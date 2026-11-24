class Contact:
    def __init__(self):
        self._email = ""
    @property
    def email(self):
        return self._email
    @email.setter
    def email(self, v):
        if "@" in v:
            self._email = v 
        else:
            self._email = "noto'g'ri"
c = Contact()
c.email = input()
print(c.email)
