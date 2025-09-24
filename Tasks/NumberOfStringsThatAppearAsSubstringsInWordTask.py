def numOfStrings(self, patterns, word):
    """
    :type patterns: List[str]
    :type word: str
    :rtype: int
    """

    result = 0

    for i in patterns:
        if word.__contains__(i):
            result += 1

    return result
#https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/