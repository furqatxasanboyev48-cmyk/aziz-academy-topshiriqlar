import unittest
def is_palindrome(s):
    return s == s[::-1]
class TestPalindrome(unittest.TestCase):
    def test_true(self):
        self.assertTrue(is_palindrome("abba"))
    def test_false(self):
        self.assertFalse(is_palindrome("abc"))
s = input().strip()
print("YES" if is_palindrome(s) else "NO")