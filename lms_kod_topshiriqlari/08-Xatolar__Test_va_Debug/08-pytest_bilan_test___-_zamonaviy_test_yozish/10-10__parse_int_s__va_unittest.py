import unittest
def parse_int(s):
    return int(s)
class TestParseInt(unittest.TestCase):
    def test_ok(self):
        self.assertEqual(parse_int("10"), 10)
    def test_bad(self):
        self.assertRaises(ValueError, parse_int, "abc")
s = input().strip()
try:
    print(parse_int(s))
except ValueError:
    print("BAD")
    