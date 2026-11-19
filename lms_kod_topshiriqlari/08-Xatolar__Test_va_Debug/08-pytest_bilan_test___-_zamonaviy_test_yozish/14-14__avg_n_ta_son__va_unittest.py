import unittest
def avg(lst):
    if not lst:
        return 0.0
    return sum(lst) / len(lst)
class TestAvg(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(avg([1, 2, 3]), 2.0)
    def test_empty(self):
        self.assertEqual(avg([]), 0.0)
n = int(input())
lst = [int(input()) for _ in range(n)]
print(f"{avg(lst):.2f}")
