import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Tasks'))

from Tasks.OneBitAndTwoBitCharactersTask import isOneBitCharacter


class OneBitAndTwoBitCharactersTests(unittest.TestCase):

    def test_first_case(self):
        n = [1,0,0]
        expected_output = True
        result = isOneBitCharacter(n)
        self.assertEqual(result, expected_output)

    def test_second_case(self):
        n = [1,1,1,0]
        expected_output = False
        result = isOneBitCharacter(n)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()



#OneBitAndTwoBitCharactersTask