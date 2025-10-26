import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Tasks'))

from Tasks.ConvertIntegerToTheSumOfTwoNoZeroIntegersTask import getNoZeroIntegers


class ConvertIntegerToTheSumOfTwoNoZeroIntegersTests(unittest.TestCase):

    def test_first_case(self):
        n = 2
        expected_output = [1,1]
        result = getNoZeroIntegers(n)
        self.assertEqual(result, expected_output)

    def test_second_case(self):
        n = 11
        expected_output = [2,9]
        result = getNoZeroIntegers(n)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()