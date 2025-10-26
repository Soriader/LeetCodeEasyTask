import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Tasks'))

from Tasks.ExcelSheetColumnTitleTask import convertToTitle


class ExcelSheetColumnTitleTests(unittest.TestCase):

    def test_first_case(self):
        n = 1
        expected_output = "A"
        result = convertToTitle(n)
        self.assertEqual(result, expected_output)

    def test_second_case(self):
        n = 28
        expected_output = "AB"
        result = convertToTitle(n)
        self.assertEqual(result, expected_output)

    def test_third_case(self):
        n = 701
        expected_output = "ZY"
        result = convertToTitle(n)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()