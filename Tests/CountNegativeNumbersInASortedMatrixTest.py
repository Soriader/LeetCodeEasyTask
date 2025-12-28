import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Tasks'))

from Tasks.CountNegativeNumbersInASortedMatrixTask import countNegatives


class CountNegativeNumbersInASortedMatrixTests(unittest.TestCase):

    def test_first_case(self):
        n = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
        expected_output = 8
        result = countNegatives(self, n)
        self.assertEqual(result, expected_output)

    def test_second_case(self):
        n = [[3,2],[1,0]]
        expected_output = 0
        result = countNegatives(self, n)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()
#CountNegativeNumbersInASortedMatrixTask