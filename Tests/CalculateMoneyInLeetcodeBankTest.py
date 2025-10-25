import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Tasks'))

from Tasks.CalculateMoneyInLeetcodeBankTask import totalMoney

class CalculateMoneyInBank(unittest.TestCase):

    def test_case_4(self):
        n = 4
        expected_output = 10
        result = totalMoney(n)
        self.assertEqual(result, expected_output)

    def test_case_10(self):
        n = 10
        expected_output = 37
        result = totalMoney(n)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()