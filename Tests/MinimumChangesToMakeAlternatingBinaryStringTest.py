import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Tasks'))

from Tasks.MinimumChangesToMakeAlternatingBinaryStringTask import minOperations


class MinimumChangesToMakeAlternatingBinaryStringTests(unittest.TestCase):

    def test_first_case(self):
        n = "0100"
        expected_output = 1
        result = minOperations(self, n)
        self.assertEqual(result, expected_output)

    def test_second_case(self):
        n = "10"
        expected_output = 0
        result = minOperations(self, n)
        self.assertEqual(result, expected_output)

    def test_third_case(self):
        n = "1111"
        expected_output = 2
        result = minOperations(self, n)
        self.assertEqual(result, expected_output)

    def test_forth_case(self):
        n = "10010100"
        expected_output = 3
        result = minOperations(self, n)
        self.assertEqual(result, expected_output)


if __name__ == '__main__':
    unittest.main()
