import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Tasks'))

from Tasks.CountBinarySubstringsTask import countBinarySubstrings


class CountBinarySubstringsTests(unittest.TestCase):

    def test_first_case(self):
        n = "00110011"
        expected_output = 6
        result = countBinarySubstrings(self, n)
        self.assertEqual(result, expected_output)

    def test_second_case(self):
        n = "10101"
        expected_output = 4
        result = countBinarySubstrings(self, n)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()
