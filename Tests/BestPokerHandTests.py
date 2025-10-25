import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Tasks'))

from Tasks.BestPokerHandTask import Solution

class TestBestPokerHand(unittest.TestCase):


    def setUp(self):
        self.solution = Solution()

    def test_flush(self):
        """Test Flush - all suits the same"""
        ranks = [13, 2, 3, 1, 9]
        suits = ["a", "a", "a", "a", "a"]
        result = self.solution.bestHand(ranks, suits)
        self.assertEqual(result, "Flush")

    def test_three_of_a_kind(self):
        """Test Three of a Kind"""
        ranks = [4, 4, 4, 2, 3]
        suits = ["a", "b", "c", "d", "e"]
        result = self.solution.bestHand(ranks, suits)
        self.assertEqual(result, "Three of a Kind")

    def test_pair(self):
        """Test Pair"""
        ranks = [10, 10, 2, 3, 4]
        suits = ["a", "b", "c", "d", "e"]
        result = self.solution.bestHand(ranks, suits)
        self.assertEqual(result, "Pair")

    def test_high_card(self):
        """Test High Card"""
        ranks = [2, 5, 7, 9, 11]
        suits = ["a", "b", "c", "d", "e"]
        result = self.solution.bestHand(ranks, suits)
        self.assertEqual(result, "High Card")

    def test_full_house_counts_as_three(self):
        """Test that Full House returns Three of a Kind"""
        ranks = [5, 5, 5, 2, 2]  # Three of a kind + Pair
        suits = ["a", "b", "c", "d", "e"]
        result = self.solution.bestHand(ranks, suits)
        self.assertEqual(result, "Three of a Kind")

    def test_two_pairs_counts_as_pair(self):
        """Test that Two Pairs returns Pair"""
        ranks = [3, 3, 5, 5, 7]  # Two pairs
        suits = ["a", "b", "c", "d", "e"]
        result = self.solution.bestHand(ranks, suits)
        self.assertEqual(result, "Pair")

    def test_flush_beats_three_of_a_kind(self):
        """Test that Flush beats Three of a Kind"""
        ranks = [4, 4, 4, 2, 2]  # Could be Three of a Kind
        suits = ["a", "a", "a", "a", "a"]  # But it's Flush
        result = self.solution.bestHand(ranks, suits)
        self.assertEqual(result, "Flush")

    def test_three_beats_pair(self):
        """Test that Three of a Kind beats Pair"""
        ranks = [6, 6, 6, 5, 7]  # Three of a Kind
        suits = ["a", "b", "c", "d", "e"]
        result = self.solution.bestHand(ranks, suits)
        self.assertEqual(result, "Three of a Kind")

    def test_edge_case_all_same_rank_but_different_suits(self):
        """Test all same ranks but different suits"""
        ranks = [7, 7, 7, 7, 7]
        suits = ["a", "b", "c", "d", "e"]
        result = self.solution.bestHand(ranks, suits)
        self.assertEqual(result, "Three of a Kind")

    def test_edge_case_all_same_rank_and_suit(self):
        """Test all same ranks and same suit"""
        ranks = [1, 1, 1, 1, 1]
        suits = ["h", "h", "h", "h", "h"]
        result = self.solution.bestHand(ranks, suits)
        self.assertEqual(result, "Flush")

    def test_minimum_cards(self):
        """Test with minimum number of cards"""
        ranks = [1, 1]
        suits = ["a", "a"]
        result = self.solution.bestHand(ranks, suits)
        self.assertEqual(result, "Flush")

    def test_isFlush_method(self):
        """Test isFlush method directly"""
        self.assertTrue(self.solution.isFlush(["a", "a", "a", "a", "a"]))
        self.assertFalse(self.solution.isFlush(["a", "a", "b", "a", "a"]))

    def test_isThree_method(self):
        """Test isThree method directly"""
        self.assertTrue(self.solution.isThree([1, 1, 1, 2, 3]))
        self.assertTrue(self.solution.isThree([1, 1, 1, 1, 2]))  # Four of a kind
        self.assertFalse(self.solution.isThree([1, 1, 2, 3, 4]))

    def test_isPair_method(self):
        """Test isPair method directly"""
        self.assertTrue(self.solution.isPair([1, 1, 2, 3, 4]))
        self.assertTrue(self.solution.isPair([1, 1, 2, 2, 3]))  # Two pairs
        self.assertFalse(self.solution.isPair([1, 2, 3, 4, 5]))

if __name__ == '__main__':
    unittest.main()