import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Tasks'))

from Tasks.CountElementsWithMaximumFrequencyTask import maxFrequencyElements


class CountElementsWithMaximumFrequencyTests(unittest.TestCase):

    def test_first_case(self):
        n = [1,2,2,3,1,4]
        expected_output = 4
        result = maxFrequencyElements(n)
        self.assertEqual(result, expected_output)

    def test_second_case(self):
        n = [1,2,3,4,5]
        expected_output = 5
        result = maxFrequencyElements(n)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()