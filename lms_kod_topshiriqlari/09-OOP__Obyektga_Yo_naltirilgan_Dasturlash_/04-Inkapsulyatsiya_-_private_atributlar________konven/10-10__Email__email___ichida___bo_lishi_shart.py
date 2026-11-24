class Email:
    def __init__(self, email):
        self._email = email
    def set_email(self, x):
        self._email = x 
    def get_email(self):
        return self._email
def valid(e):
    return bool(e) and "@" in e 
email = input().strip()
new_email = input().strip()
if valid(email) and valid(new_email):
    e = Email(email)
    e.set_email(new_email)
    print(e.get_email())
else:
    print("BAD")