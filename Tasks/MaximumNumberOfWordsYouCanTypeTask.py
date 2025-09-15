def canBeTypedWords(self, text, brokenLetters):
    """
    :type text: str
    :type brokenLetters: str
    :rtype: int
    """
    list_of_words = text.split()
    broken_chars = list(brokenLetters)
    result = 0

    for word in list_of_words:
        contains_broken = any(char in word for char in broken_chars)

        if not contains_broken:
            result += 1

    return result

#https://leetcode.com/problems/maximum-number-of-words-you-can-type/description/?envType=daily-question&envId=2025-09-15