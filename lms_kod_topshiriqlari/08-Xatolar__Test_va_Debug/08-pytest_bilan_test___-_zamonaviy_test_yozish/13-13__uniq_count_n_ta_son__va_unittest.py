import unittest
def uniq_count(lst):
    return len(set(lst))
class TestUniq(unittest.TestCase):
    def test_dup(self):
        self.assertEqual(uniq_count([1, 1, 2]), 2)
    def test_empty(self):
        self.assertEqual(uniq_count([]), 0)
n = int(input())
lst = [int(input()) for _ in range(n)]
print(uniq_count(lst))