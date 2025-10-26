import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Tasks'))

from Tasks.CountingBitsTask import countBits


class CountingBitsTests(unittest.TestCase):

    def test_first_case(self):
        n = 2
        expected_output = [0,1,1]
        result = countBits(n)
        self.assertEqual(result, expected_output)

    def test_second_case(self):
        n = 5
        expected_output = [0,1,1,2,1,2]
        result = countBits(n)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()