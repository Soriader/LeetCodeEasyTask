import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Tasks'))

from Tasks.SpecialPositionsInABinaryMatrixTask import numSpecial


class SpecialPositionsInABinaryMatrixTests(unittest.TestCase):

    def test_first_case(self):
        n = [[1,0,0],[0,0,1],[1,0,0]]
        expected_output = 1
        result = numSpecial(n)
        self.assertEqual(result, expected_output)

    def test_second_case(self):
        n = [[1,0,0],[0,1,0],[0,0,1]]
        expected_output = 3
        result = numSpecial(n)
        self.assertEqual(result, expected_output)


if __name__ == '__main__':
    unittest.main()

#SpecialPositionsInABinaryMatrixTask