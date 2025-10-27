def checkIfPangram(sentence):
    """
    :type sentence: str
    :rtype: bool
    """

    no_duplicate = ''.join(dict.fromkeys(sentence))
    sorted_result = ''.join(sorted(no_duplicate))
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    return sorted_result == alphabet

#https://leetcode.com/problems/check-if-the-sentence-is-pangram/description/