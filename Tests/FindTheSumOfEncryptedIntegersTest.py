import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Tasks'))

from Tasks.FindTheSumOfEncryptedIntegersTask import sumOfEncryptedInt


class FindTheSumOfEncryptedIntegersTests(unittest.TestCase):

    def test_first_case(self):
        n = [1,2,3]
        expected_output = 6
        result = sumOfEncryptedInt(n)
        self.assertEqual(result, expected_output)

    def test_second_case(self):
        n = [10,21,31]
        expected_output = 66
        result = sumOfEncryptedInt(n)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()