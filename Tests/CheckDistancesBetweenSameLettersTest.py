import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Tasks'))

from Tasks.CheckDistancesBetweenSameLettersTask import checkDistances


class CheckDistancesBetweenSameLettersTests(unittest.TestCase):

    def test_first_case(self):
        s = "abaccb"
        distance = [1,3,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        expected_output = True
        result = checkDistances(s, distance)
        self.assertEqual(result, expected_output)

    def test_second_case(self):
        s = "aa"
        distance = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        expected_output = False
        result = checkDistances(s, distance)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()