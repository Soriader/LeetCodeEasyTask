import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Tasks'))

from Tasks.ValidPalindromeTask import isPalindrome


class ClimbingStairsTests(unittest.TestCase):

    def test_first_case(self):
        n = "A man, a plan, a canal: Panama"
        expected_output = True
        result = isPalindrome(self, n)
        self.assertEqual(result, expected_output)

    def test_second_case(self):
        n = "race a car"
        expected_output = False
        result = isPalindrome(self, n)
        self.assertEqual(result, expected_output)

    def test_third_case(self):
        n = ""
        expected_output = True
        result = isPalindrome(self, n)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()

#ValidPalindromeTask