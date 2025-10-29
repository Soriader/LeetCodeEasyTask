import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Tasks'))

from Tasks.SmallestNumberWithAllSetBitsTask import smallestNumber


class SmallestNumberWithAllSetBitsTests(unittest.TestCase):

    def test_first_case(self):
        n = 5
        expected_output = 7
        result = smallestNumber(n)
        self.assertEqual(result, expected_output)

    def test_second_case(self):
        n = 3
        expected_output = 3
        result = smallestNumber(n)
        self.assertEqual(result, expected_output)

    def test_third_case(self):
        n = 10
        expected_output = 15
        result = smallestNumber(n)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()