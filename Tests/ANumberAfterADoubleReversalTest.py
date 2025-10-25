import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Tasks'))

from Tasks.ANumberAfterADoubleReversalTask import isSameAfterReversals

class ANumberAfterADoubleReversalTests(unittest.TestCase):

    def test_case_526(self):
        n = 526
        expected_output = True
        result = isSameAfterReversals(n)
        self.assertEqual(result, expected_output)

    def test_case_1800(self):
        n = 1800
        expected_output = False
        result = isSameAfterReversals(n)
        self.assertEqual(result, expected_output)

    def test_case_0(self):
        n = 0
        expected_output = True
        result = isSameAfterReversals(n)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()