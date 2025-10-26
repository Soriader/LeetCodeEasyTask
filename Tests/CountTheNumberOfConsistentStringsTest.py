import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Tasks'))

from Tasks.CountTheNumberOfConsistentStringsTask import countConsistentStrings


class CountTheNumberOfConsistentStringsTest(unittest.TestCase):

    def test_first_case(self):
        allowed = "ab"
        words = ["ad", "bd", "aaab", "baa", "badab"]
        expected_output = 2
        result = countConsistentStrings(allowed, words)
        self.assertEqual(result, expected_output)

    def test_second_case(self):
        allowed = "abc"
        words = ["a", "b", "c", "ab", "ac", "bc", "abc"]
        expected_output = 7
        result = countConsistentStrings(allowed, words)
        self.assertEqual(result, expected_output)

    def test_third_case(self):
        allowed = "cad"
        words = ["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"]
        expected_output = 4
        result = countConsistentStrings(allowed, words)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()