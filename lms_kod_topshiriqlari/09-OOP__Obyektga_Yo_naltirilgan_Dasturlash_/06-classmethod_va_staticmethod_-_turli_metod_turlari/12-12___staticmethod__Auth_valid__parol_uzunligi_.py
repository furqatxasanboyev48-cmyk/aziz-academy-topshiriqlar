class Auth:
    @staticmethod
    def valid(pw):
        return "Ha" if len(pw) >= 6 else "Yo'q"
print(Auth.valid(input()))