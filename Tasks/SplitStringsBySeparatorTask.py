def splitWordsBySeparator(self, words, separator):
    """
    :type words: List[str]
    :type separator: str
    :rtype: List[str]
    """

    result = []
    for word in words:
        parts = word.split(separator)
        for part in parts:
            if part:
                result.append(part)
    return result

#https://leetcode.com/problems/split-strings-by-separator/description/