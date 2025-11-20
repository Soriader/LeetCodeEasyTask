import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Tasks'))

from Tasks.RotateStringTask import rotateString


class RotateStringTests(unittest.TestCase):

    def test_first_case(self):
        s = "abcde"
        goal = "cdeab"
        expected_output = True
        result = rotateString(s, goal)
        self.assertEqual(result, expected_output)

    def test_second_case(self):
        s = "abcde"
        goal = "abced"
        expected_output = False
        result = rotateString(s, goal)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()