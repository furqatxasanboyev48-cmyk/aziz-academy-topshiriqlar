class User:
    count = 0
    def __init__(self, username):
        self.username = username.strip()
        if self.username:
            User.count += 1 
try:
    n = int(input().strip())
except ValueError:
    print("BAD")
else:
    if n < 0:
        print("BAD")
    else:
        ok = True
        for _ in range(n):
            u = User(input())
            if not u.username:
                ok = False
                break
        print(f"COUNT={User.count}" if ok else "BAD")        
    
            