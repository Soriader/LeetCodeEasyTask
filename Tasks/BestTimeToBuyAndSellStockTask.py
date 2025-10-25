def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if not prices:
        return 0

    min_price = float('inf')
    result = 0

    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > result:
            result = price - min_price

    return result

#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/