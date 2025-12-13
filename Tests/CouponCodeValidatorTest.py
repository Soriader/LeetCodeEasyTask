import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Tasks'))

from Tasks.CouponCodeValidatorTask import validateCoupons

class CouponCodeValidatorTests(unittest.TestCase):

    def test_first_case(self):
        code = ["SAVE20", "", "PHARMA5", "SAVE@20"]
        business_line = ["restaurant", "grocery", "pharmacy","restaurant"]
        is_active = [True, True, True, True]
        expected_output = ["PHARMA5","SAVE20"]
        result = validateCoupons(self, code, business_line, is_active)
        self.assertEqual(result, expected_output)

    def test_second_case(self):
        code = ["GROCERY15","ELECTRONICS_50","DISCOUNT10"]
        business_line = ["grocery","electronics","invalid"]
        is_active = [False,True,True]
        expected_output = ["ELECTRONICS_50"]
        result = validateCoupons(self, code, business_line, is_active)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()