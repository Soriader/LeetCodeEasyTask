import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Tasks'))

from Tasks.MinimumOperationsToMakeArraySumDivisibleByKTask import minOperations


class MinimumOperationsToMakeArraySumDivisibleByKTest(unittest.TestCase):

    def test_first_case(self):
        n = [3,9,7]
        k = 5
        expected_output = 4
        result = minOperations(self, n, k)
        self.assertEqual(result, expected_output)

    def test_second_case(self):
        n = [3,2]
        k = 6
        expected_output = 5
        result = minOperations(self, n, k)
        self.assertEqual(result, expected_output)

    def test_third_case(self):
        n = [4,1,3]
        k = 4
        expected_output = 0
        result = minOperations(self, n, k)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()




#MinimumOperationsToMakeArraySumDivisibleByKTask