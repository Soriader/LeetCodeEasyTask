def pivotIndex(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    for i in range(len(nums)):
        left_sum = sum(nums[:i])
        right_sum = sum(nums[i + 1:])

        if left_sum == right_sum:
            return i

    return -1

#https://leetcode.com/problems/find-pivot-index/description/