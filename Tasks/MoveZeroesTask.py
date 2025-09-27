def moveZeroes(self, nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    non_zeros = [num for num in nums if num != 0]
    zeros_count = len(nums) - len(non_zeros)

    nums[:] = non_zeros + [0] * zeros_count

#https://leetcode.com/problems/move-zeroes/description/