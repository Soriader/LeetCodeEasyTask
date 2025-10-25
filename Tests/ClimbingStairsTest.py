import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Tasks'))

from Tasks.ClimbingStairsTask import climbStairs


class ClimbingStairsTests(unittest.TestCase):

    def test_first_case(self):
        n = 2
        expected_output = 2
        result = climbStairs(n)
        self.assertEqual(result, expected_output)

    def test_second_case(self):
        n = 3
        expected_output = 3
        result = climbStairs(n)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()