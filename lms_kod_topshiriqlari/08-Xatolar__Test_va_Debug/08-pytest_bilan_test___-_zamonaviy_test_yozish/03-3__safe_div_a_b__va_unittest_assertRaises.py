import unittest
def safe_div(a, b):
    if b == 0:
        raise ZeroDivisionError
    return a / b 
class TestSafeDiv(unittest.TestCase):
    def test_ok(self):
        self.assertEqual(sate_div(10, 2), 5.0)
    def test_zero(self):
        self.assertRaise(ZeroDivisionError, safe_div, 1, 0)
a, b = map(int, input().split())
try:
    print(f"{safe_div(a, b):.2f}")
except ZeroDivisionError:
    print("DIV0")