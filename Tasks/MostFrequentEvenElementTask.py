from collections import Counter

def mostFrequentEven(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    freq = Counter(x for x in nums if x % 2 == 0)

    if not freq:
        return -1

    max_freq = max(freq.values())

    return min(num for num, count in freq.items() if count == max_freq)

#https://leetcode.com/problems/most-frequent-even-element/description/