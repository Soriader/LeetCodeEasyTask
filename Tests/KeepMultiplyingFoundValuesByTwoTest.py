import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Tasks'))

from Tasks.KeepMultiplyingFoundValuesByTwoTask import findFinalValue


class KeepMultiplyingFoundValuesByTwoTests(unittest.TestCase):

    def test_first_case(self):
        nums = [5,3,6,1,12]
        original = 3
        expected_output = 24
        result = findFinalValue(nums, original)
        self.assertEqual(result, expected_output)

    def test_second_case(self):
        nums = [2,7,9]
        original = 4
        expected_output = 4
        result = findFinalValue(nums, original)
        self.assertEqual(result, expected_output)


if __name__ == '__main__':
    unittest.main()

#KeepMultiplyingFoundValuesByTwoTask