def buyChoco(self, prices, money):
    """
    :type prices: List[int]
    :type money: int
    :rtype: int
    """

    cheapest_chocolate = min(prices)
    prices.remove(cheapest_chocolate)
    change = money - cheapest_chocolate
    prices.sort()

    for choco in prices:

        if choco <= change:
            change -= choco
            return change

    return money

#https://leetcode.com/problems/buy-two-chocolates/description/