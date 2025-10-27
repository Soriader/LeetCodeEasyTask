import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Tasks'))

from Tasks.CheckIfTheSentenceIsPangramTask import checkIfPangram


class CheckIfTheSentenceIsPangramTests(unittest.TestCase):

    def test_first_case(self):
        n = "thequickbrownfoxjumpsoverthelazydog"
        expected_output = True
        result = checkIfPangram(n)
        self.assertEqual(result, expected_output)

    def test_second_case(self):
        n = "leetcode"
        expected_output = False
        result = checkIfPangram(n)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()