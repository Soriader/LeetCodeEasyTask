import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Tasks'))

from Tasks.BuyTwoChocolatesTask import buyChoco


class BuyTwoChocolatesTests(unittest.TestCase):

    def test_first_case(self):
        prices = [1,2,2]
        money = 3
        expected_output = 0
        result = buyChoco(prices, money)
        self.assertEqual(result, expected_output)

    def test_second_case(self):
        prices = [3,2,3]
        money = 3
        expected_output = 3
        result = buyChoco(prices, money)
        self.assertEqual(result, expected_output)


if __name__ == '__main__':
    unittest.main()