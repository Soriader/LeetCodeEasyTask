import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Tasks'))

from Tasks.MirrorDistanceOfAnIntegerTask import mirrorDistance


class MirrorDistanceOfAnIntegerTests(unittest.TestCase):

    def test_first_case(self):
        n = 25
        expected_output = 27
        result = mirrorDistance(self, n)
        self.assertEqual(result, expected_output)

    def test_second_case(self):
        n = 10
        expected_output = 9
        result = mirrorDistance(self, n)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()