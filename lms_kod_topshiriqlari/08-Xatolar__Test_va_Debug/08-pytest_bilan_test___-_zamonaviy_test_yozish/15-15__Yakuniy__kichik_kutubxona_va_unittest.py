import sys
import unittest
def add(a, b):
    return a + b 
def is_even(n):
    return n % 2 == 0
def safe_div(a, b):
    if b == 0:
        raise ZeroDivisionError
    return a / b 
class TestLib(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)
    def test_is_even(self):
        self.assertTrue(is_even(2))
        self.assertFalse(is_even(3))
    def test_safe_div(self):
        self.assertEqual(safe_div(10, 2), 5.0)
        self.assertRaises(ZeroDivisionError, safe_div, 1, 0)
data = sys.stdin.read().split("\n")
op = data[0].strip()
if op == "ADD":
    print(add(int(data[1]), int(data[2])))
elif op == "EVEN":
    print("EVEN" if is_even(int(data[1])) else "ODD")
else:
    try:
        print(f"{safe_div(float(data[1]), float(data[2])):.2f}")
    except ZeroDivisionError:
        print("DIV0")
    

    

        
        