import unittest
def count_vowels(s):
    return sum(1 for ch in s.lower() if ch in "aeiou")
class TestVowels(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(count_vowels("hello"), 2)
    def test_none(self):
        self.assertEqual(count_vowels("xyz"), 0)
s = input().strip()
print(count_vowels(s))
    
    