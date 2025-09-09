def isAnagram(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """

    dic_s = {}
    dic_t = {}

    for ch in s:
        dic_s[ch] = dic_s.get(ch, 0) + 1

    for ch in t:
        dic_t[ch] = dic_t.get(ch, 0) + 1

    return dic_s == dic_t

#https://leetcode.com/problems/valid-anagram/description/