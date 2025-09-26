def majorityElement(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    dict = {}
    result = 0
    for num in nums:
        if num in dict:
            dict[num] += 1
        else:
            dict[num] = 1

    check_value = len(nums) / 2

    for key, value in dict.items():
        if value > check_value:
            result = key

    return result

#https://leetcode.com/problems/majority-element/description/