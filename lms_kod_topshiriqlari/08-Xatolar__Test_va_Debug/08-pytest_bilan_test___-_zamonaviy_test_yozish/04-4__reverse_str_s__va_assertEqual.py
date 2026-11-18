import unittest
def reverse_str(s):
    return s[::-1]
class TestReverse(unittest.TestCase):
    def test_reverse(self):
        self.assertEqual(reverse_str("abc"),"cba")
        self.assertEqual(reverse_str("a"),"a")
s = input().strip()
print(reverse_str(s))