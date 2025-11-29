def minOperations(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """

    return sum(nums) % k

#https://leetcode.com/problems/minimum-operations-to-make-array-sum-divisible-by-k/description/?envType=daily-question&envId=2025-11-29