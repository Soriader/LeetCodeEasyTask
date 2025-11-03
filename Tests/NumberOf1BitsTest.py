#NumberOf1BitsTask

import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Tasks'))

from Tasks.NumberOf1BitsTask import hammingWeight

class NumberOf1BitsTests(unittest.TestCase):

    def test_first_case(self):
        n = 11
        expected_output = 3
        result = hammingWeight(n)
        self.assertEqual(result, expected_output)

    def test_second_case(self):
        n = 128
        expected_output = 1
        result = hammingWeight(n)
        self.assertEqual(result, expected_output)

    def test_third_case(self):
        n = 2147483645
        expected_output = 30
        result = hammingWeight(n)
        self.assertEqual(result, expected_output)
if __name__ == '__main__':
    unittest.main()