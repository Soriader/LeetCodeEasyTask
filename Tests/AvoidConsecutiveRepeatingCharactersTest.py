import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Tasks'))

from Tasks.AvoidConsecutiveRepeatingCharactersTask import modifyString

class AvoidConsecutiveRepeatingCharactersTests(unittest.TestCase):

    def first_case(self):
        s = "?zs"
        expected_output = "azs"
        result = modifyString(s)
        self.assertEqual(result, expected_output)

    def second_case(self):
        s = "ubv?w"
        expected_output = "ubvaw"
        result = modifyString(s)
        self.assertEqual(result, expected_output)


if __name__ == '__main__':
    unittest.main()
