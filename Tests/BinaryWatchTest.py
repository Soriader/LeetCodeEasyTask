import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Tasks'))

from Tasks.BinaryWatchTask import readBinaryWatch


class BinaryWatchTests(unittest.TestCase):

    def test_first_case(self):
        n = 1
        expected_output = ["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]
        result = readBinaryWatch(self, n)
        self.assertEqual(result, expected_output)

    def test_second_case(self):
        n = 9
        expected_output = []
        result = readBinaryWatch(self, n)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()

#BinaryWatchTask