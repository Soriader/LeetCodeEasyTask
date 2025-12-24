import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Tasks'))

from Tasks.AppleRedistributionIntoBoxesTask import minimumBoxes


class AppleRedistributionIntoBoxesTests(unittest.TestCase):

    def test_first_case(self):
        apple = [1,3,2]
        capacity = [4,3,1,5,2]
        expected_output = 2
        result = minimumBoxes(self, apple, capacity)
        self.assertEqual(result, expected_output)

    def test_second_case(self):
        apple = [5,5,5]
        capacity = [2,4,2,7]
        expected_output = 4
        result = minimumBoxes(self, apple, capacity)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()
