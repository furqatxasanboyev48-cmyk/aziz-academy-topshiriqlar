import unittest 
def add(a, b):
    return a + b 
class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2),3)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)
a, b = map(int, input().split())
print(add(a, b))