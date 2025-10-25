import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Tasks'))

from Tasks.BestTimeToBuyAndSellStockTask import maxProfit


class BestTimeToBuyAndSellStockTests(unittest.TestCase):

    def test_first_case(self):
        prices = [7,1,5,3,6,4]
        expected_output = 5
        result = maxProfit(prices)
        self.assertEqual(result, expected_output)


    def test_second_case(self):
        prices = [7,6,4,3,1]
        expected_output = 0
        result = maxProfit(prices)
        self.assertEqual(result, expected_output)


if __name__ == '__main__':
    unittest.main()