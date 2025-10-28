import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Tasks'))

from Tasks.SumMultiplesTask import sumOfMultiples


class SumMultiplesTests(unittest.TestCase):

    def test_first_case(self):
        n = 10
        expected_output = 40
        result = sumOfMultiples(n)
        self.assertEqual(result, expected_output)

    def test_second_case(self):
        n = 7
        expected_output = 21
        result = sumOfMultiples(n)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()