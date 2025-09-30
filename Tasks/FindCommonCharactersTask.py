from collections import Counter
def commonChars(self, words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    result = []
    counters = [Counter(word) for word in words]

    for letter in counters[0]:
        min_count = min(counter.get(letter, 0) for counter in counters)

        if min_count > 0:
            result.extend([letter] * min_count)

    return result

#https://leetcode.com/problems/find-common-characters/description/?source=submission-noac