def minElement(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    result = []

    for num in nums:
        result.append(sum(list(map(int, str(num)))))

    return min(result)

#https://leetcode.com/problems/minimum-element-after-replacement-with-digit-sum/description/