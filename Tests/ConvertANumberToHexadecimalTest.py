import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Tasks'))

from Tasks.ConvertANumberToHexadecimalTask import toHex


class ConvertANumberToHexadecimalTests(unittest.TestCase):

    def test_first_case(self):
        n = 26
        expected_output = "1a"
        result = toHex(n)
        self.assertEqual(result, expected_output)

    def test_second_case(self):
        n = -1
        expected_output = "ffffffff"
        result = toHex(n)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()