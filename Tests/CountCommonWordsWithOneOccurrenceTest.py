import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Tasks'))

from Tasks.CountCommonWordsWithOneOccurrenceTask import countWords


class CountCommonWordsWithOneOccurrenceTests(unittest.TestCase):

    def test_first_case(self):
        words1 = ["leetcode", "is", "amazing", "as", "is"]
        words2 = ["amazing", "leetcode", "is"]
        expected_output = 2
        result = countWords(words1, words2)
        self.assertEqual(result, expected_output)

    def test_second_case(self):
        words1 = ["b","bb","bbb"]
        words2 = ["a","aa","aaa"]
        expected_output = 0
        result = countWords(words1, words2)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()