from collections import Counter

class Solution(object):
    def bestHand(self, ranks, suits):
        """
        :type ranks: List[int]
        :type suits: List[str]
        :rtype: str
        """
        if self.isFlush(suits):
            return "Flush"

        if self.isThree(ranks):
            return "Three of a Kind"

        if self.isPair(ranks):
            return "Pair"

        return "High Card"

    def isFlush(self, suits):

        the_same = suits[0]

        for suit in suits:
            if suit != the_same:
                return False

        return True

    def isThree(self, ranks):

        return any(count >= 3 for count in Counter(ranks).values())

    def isPair(self, ranks):
        return any(count >= 2 for count in Counter(ranks).values())

    # https://leetcode.com/problems/best-poker-hand/description/