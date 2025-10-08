def isSubsequence(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """

    if s == "":
        return True

    letters_from_s = list(s)
    iterator = 0
    for letter in t:
        if letter == letters_from_s[iterator]:
            iterator += 1
            if iterator == len(s):
                break

    return iterator == len(s)

#https://leetcode.com/problems/is-subsequence/description/