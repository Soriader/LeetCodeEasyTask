def findGCD(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    smallest = min(nums)
    largest = max(nums)

    if(largest % smallest == 0):
        return smallest

    divisor = smallest

    while divisor > 0:
        divisor -= 1
        if largest % divisor == 0 and smallest % divisor == 0:
            return divisor


    return 1

#https://leetcode.com/problems/find-greatest-common-divisor-of-array/description/