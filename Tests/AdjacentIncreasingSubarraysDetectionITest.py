import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Tasks'))

from Tasks.AdjacentIncreasingSubarraysDetectionITask import hasIncreasingSubarrays


class AdjacentIncreasingSubarraysDetectionI(unittest.TestCase):

    def test_first_case(self):
        nums = [2,5,7,8,9,2,3,4,3,1]
        k = 3
        expected_output = True
        result = hasIncreasingSubarrays(nums, k)
        self.assertEqual(result, expected_output)


    def test_edge_cases(self):
        nums = [1,2,3,4,4,4,4,5,6,7]
        k = 5
        expected_output = False
        result = hasIncreasingSubarrays(nums, k)
        self.assertEqual(result, expected_output)


if __name__ == '__main__':
    unittest.main()

