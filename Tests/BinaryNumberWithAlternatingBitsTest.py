import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Tasks'))

from Tasks.BinaryNumberWithAlternatingBitsTask import hasAlternatingBits


class BinaryNumberWithAlternatingBitsTests(unittest.TestCase):

    def test_first_case(self):
        n = 5
        expected_output = True
        result = hasAlternatingBits(self, n)
        self.assertEqual(result, expected_output)

    def test_second_case(self):
        n = 7
        expected_output = False
        result = hasAlternatingBits(self, n)
        self.assertEqual(result, expected_output)

    def test_third_case(self):
        n = 11
        expected_output = False
        result = hasAlternatingBits(self, n)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()
