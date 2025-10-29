import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Tasks'))

from Tasks.NumberOfCommonFactorsTask import commonFactors


class NumberOfCommonFactorsTests(unittest.TestCase):

    def test_first_case(self):
        a = 12
        b = 6
        expected_output = 4
        result = commonFactors(a,b)
        self.assertEqual(result, expected_output)

    def test_second_case(self):
        a = 25
        b = 30
        expected_output = 2
        result = commonFactors(a,b)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()