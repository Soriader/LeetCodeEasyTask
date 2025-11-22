import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Tasks'))

from Tasks.AllElementsDivisibleByThreeTask import minimumOperations


class AllElementsDivisibleByThreeTests(unittest.TestCase):

    def test_first_case(self):
        n = [1,2,3,4]
        expected_output = 3
        result = minimumOperations(self, n)
        self.assertEqual(result, expected_output)

    def test_second_case(self):
        n = [3,6,9]
        expected_output = 0
        result = minimumOperations(self, n)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()

#AllElementsDivisibleByThreeTask