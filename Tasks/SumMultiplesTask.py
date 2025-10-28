def sumOfMultiples(n):
    """
    :type n: int
    :rtype: int
    """
    return sum(list(filter(lambda x: x % 3 == 0 or x % 5 == 0 or x % 7 == 0, range(1, n + 1))))

#https://leetcode.com/problems/sum-multiples/description/