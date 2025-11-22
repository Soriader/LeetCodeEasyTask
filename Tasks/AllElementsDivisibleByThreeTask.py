def minimumOperations(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    result = 0

    for num in nums:
        remainder = num % 3
        if remainder != 0:
            result += 1

    return result

#https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/description/?envType=daily-question&envId=2025-11-22