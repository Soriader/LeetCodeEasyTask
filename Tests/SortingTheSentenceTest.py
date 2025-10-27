import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Tasks'))

from Tasks.SortingTheSentenceTask import sortSentence


class SortingTheSentenceTests(unittest.TestCase):

    def test_first_case(self):
        n = "Myself2 Me1 I4 and3"
        expected_output = "Me Myself and I"
        result = sortSentence(n)
        self.assertEqual(result, expected_output)

    def test_second_case(self):
        n = "is2 sentence4 This1 a3"
        expected_output = "This is a sentence"
        result = sortSentence(n)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()