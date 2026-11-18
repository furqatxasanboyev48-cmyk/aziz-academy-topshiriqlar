import unittest
def max_of_two(a, b):
    return a if a > b else b 
class TestMax(unittest.TestCase):
    def test_first(self):
        self.assertEqual(max_of_two(5, 3), 5)
    def test_second(self):
        self.assertEqual(max_of_two(1, 2), 2)
a, b = map(int, input().split())
print(max_of_two(a, b))
    