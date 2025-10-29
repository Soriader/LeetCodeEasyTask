import math

def commonFactors(a, b):
    """
    :type a: int
    :type b: int
    :rtype: int
    """
    gcd = math.gcd(a, b)
    return sum(1 for i in range(1, gcd + 1) if gcd % i == 0)

#https://leetcode.com/problems/number-of-common-factors/description/
