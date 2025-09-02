def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    numDict = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in numDict:
            return [numDict[complement], i]

        numDict[num] = i

    return []
"""https://leetcode.com/problems/two-sum/description/"""