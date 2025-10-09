from collections import Counter

def countWords(self, words1, words2):
    """
    :type words1: List[str]
    :type words2: List[str]
    :rtype: int
    """

    result = 0
    words1_count = Counter(words1)
    words2_count = Counter(words2)
    checked = []

    for word, count in words1_count.items():
        if words2_count[word] == 1 and count == 1:
            result += 1
            checked.append(word)

    return result

#https://leetcode.com/problems/count-common-words-with-one-occurrence/description/