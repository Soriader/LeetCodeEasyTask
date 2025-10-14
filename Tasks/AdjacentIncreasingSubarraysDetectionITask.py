def hasIncreasingSubarrays(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """

    for i in range(len(nums) - 2 * k + 1):
        first_ok = all(nums[j] < nums[j + 1] for j in range(i, i + k - 1))

        second_ok = all(nums[j] < nums[j + 1] for j in range(i + k, i + 2 * k - 1))

        if first_ok and second_ok:
            return True

    return False

#https://leetcode.com/problems/adjacent-increasing-subarrays-detection-i/description/?envType=daily-question&envId=2025-10-14%27