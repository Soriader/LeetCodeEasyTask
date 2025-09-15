def strStr(self, haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    if not needle:
        return 0

    n = len(haystack)
    m = len(needle)

    for i in range(n - m + 1):
        match_found = True
        for j in range(m):
            if haystack[i + j] != needle[j]:
                match_found = False
                break

        if match_found:
            return i

    return -1

#https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/