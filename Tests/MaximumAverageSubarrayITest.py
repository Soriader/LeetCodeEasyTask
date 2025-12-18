import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Tasks'))

from Tasks.MaximumAverageSubarrayITask import findMaxAverage


class MaximumAverageSubarrayITests(unittest.TestCase):

    def test_first_case(self):
        nums = [1,12,-5,-6,50,3]
        k = 4
        expected_output = 12.75000
        result = findMaxAverage(self, nums, k)
        self.assertEqual(result, expected_output)

    def test_second_case(self):
        nums = [5]
        k = 1
        expected_output = 5.00000
        result = findMaxAverage(self, nums, k)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()
#MaximumAverageSubarrayITask