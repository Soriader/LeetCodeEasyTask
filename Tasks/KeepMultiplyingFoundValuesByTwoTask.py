def findFinalValue(nums, original):
    """
    :type nums: List[int]
    :type original: int
    :rtype: int
    """

    while original in nums:
        original = original * 2

    return original

#https://leetcode.com/problems/keep-multiplying-found-values-by-two/description/?envType=daily-question&envId=2025-11-19