import unittest
def gcd(a, b):
    while b:
        a,  b = b, a % b 
    return a 
class TestGcd(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(gcd(12, 18), 6)
    def test_zero(self):
        self.assertEqual(gcd(0, 5), 5)
a, b = map(int, input().split())
print(gcd(a, b))
        