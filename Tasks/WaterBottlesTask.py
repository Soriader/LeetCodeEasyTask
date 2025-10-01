def numWaterBottles(self, numBottles, numExchange):
    """
    :type numBottles: int
    :type numExchange: int
    :rtype: int
    """

    result = numBottles
    replaced_bottles = 0

    while(numBottles >= numExchange):
        replaced_bottles = numBottles // numExchange
        numBottles = replaced_bottles + (numBottles - replaced_bottles * numExchange)
        result += replaced_bottles


    return result

#https://leetcode.com/problems/water-bottles/description/?envType=daily-question&envId=2025-10-01