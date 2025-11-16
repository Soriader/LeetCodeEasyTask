#AverageValueOfEvenNumbersThatAreDivisibleByThreeTask

import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Tasks'))

from Tasks.AverageValueOfEvenNumbersThatAreDivisibleByThreeTask import averageValue


class AverageValueOfEvenNumbersThatAreDivisibleByThreeTests(unittest.TestCase):

    def test_first_case(self):
        nums = [1,3,6,10,12,15]
        expected_output = 9
        result = averageValue(nums)
        self.assertEqual(result, expected_output)

    def test_second_case(self):
        nums = [1,2,4,7,10]
        expected_output = 0
        result = averageValue(nums)
        self.assertEqual(result, expected_output)

    def test_third_case(self):
        nums = [9,3,8,4,2,5,3,8,6,1]
        expected_output = 6
        result = averageValue(nums)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()