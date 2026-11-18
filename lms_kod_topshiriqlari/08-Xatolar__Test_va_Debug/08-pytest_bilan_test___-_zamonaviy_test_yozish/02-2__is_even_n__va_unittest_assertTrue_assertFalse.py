import unittest
def is_even(n):
    return n % 2 == 0
class TestIsEven(unittest.TestCase):
    def test_even(self):
        self.assertTrue(is_even(2))
    def test_odd(self):
        self.assertFalse(is_even(3))
n = int(input())
print("EVEN" if is_even(n) else "ODD")
    