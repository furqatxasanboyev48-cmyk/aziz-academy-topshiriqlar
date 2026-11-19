import unittest
def clamp(x):
    if x < 0:
        return 0
    if x > 100:
        return 100
    return x 
class TestClamp(unittest.TestCase):
    def test_low(self):
        self.assertEqual(clamp(-1), 0)
    def test_high(self):
        self.assertEqual(clamp(101), 100)
x = int(input())
print(clamp(x))