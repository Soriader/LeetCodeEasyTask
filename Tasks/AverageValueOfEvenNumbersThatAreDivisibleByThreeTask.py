def averageValue(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    divisible_by_two_and_three = list(filter(lambda x: x % 2 == 0 and x % 3 == 0, nums))
    if not divisible_by_two_and_three:
        return 0
    return sum(divisible_by_two_and_three) // len(divisible_by_two_and_three)



#https://leetcode.com/problems/average-value-of-even-numbers-that-are-divisible-by-three/description/