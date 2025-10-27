def sortSentence(s):
    """
    :type s: str
    :rtype: str
    """

    words = s.split()
    parts_of_sentence = [word[:-1] for word in sorted(words, key=lambda x: int(x[-1]))]

    return ' '.join(parts_of_sentence)

#https://leetcode.com/problems/sorting-the-sentence/description/