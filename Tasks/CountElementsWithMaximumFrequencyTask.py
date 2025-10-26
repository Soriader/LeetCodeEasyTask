def maxFrequencyElements(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    frequency = {}
    result = 0

    for num in nums:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    highest_frequency = max(frequency.values())

    for num in frequency:
        if frequency[num] == highest_frequency:
            result += highest_frequency

    return result

#https://leetcode.com/problems/count-elements-with-maximum-frequency/description/?envType=daily-question&envId=2025-09-22