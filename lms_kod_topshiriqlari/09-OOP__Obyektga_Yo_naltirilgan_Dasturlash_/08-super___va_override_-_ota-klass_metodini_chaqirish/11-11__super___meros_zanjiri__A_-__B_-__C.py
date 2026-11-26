base = input()
class A:
    def great(self):
        return base
class B(A):
    def great(self):
        return super().great() + "-B"
class C(B):
    def great(self):
        return super().great() + "-C"
print(C().great())