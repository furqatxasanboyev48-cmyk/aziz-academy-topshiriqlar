import unittest
def sum_list(lst):
    return sum(lst)
class TestSumList(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum_list([1, 2, 3]), 6)
        self.assertEqual(sum_list([]), 0)
n = int(input())
lst = [int(input()) for _ in range(n)]
print(sum_list(lst))
        