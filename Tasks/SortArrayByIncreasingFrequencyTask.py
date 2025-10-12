from collections import Counter

def frequencySort(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """

    freq = Counter(nums)

    items = list(freq.items())

    items.sort(key=lambda x: (x[1], -x[0]))

    result = []
    for number, count in items:
        result.extend([number] * count)

    return result

#https://leetcode.com/problems/sort-array-by-increasing-frequency/description/