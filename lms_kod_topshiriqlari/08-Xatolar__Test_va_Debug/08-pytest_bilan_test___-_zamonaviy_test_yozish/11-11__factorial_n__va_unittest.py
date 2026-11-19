import unittest
def factorial(n):
    r = 1
    for i in range(2, n + 1):
        r *= i 
    return r 
class TestFactorial(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(factorial(0), 1)
    def test_five(self):
        self.assertEqual(factorial(5), 120)
n = int(input())
print(factorial(n))