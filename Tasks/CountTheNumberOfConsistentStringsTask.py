def countConsistentStrings(self, allowed, words):
    """
    :type allowed: str
    :type words: List[str]
    :rtype: int
    """

    acctual_analyses = ""
    result = 0

    for i in words:
        is_in_allowed = True
        actual_analysis = "".join(dict.fromkeys(i))

        for j in actual_analysis:
            if allowed.count(j) == 0:
                is_in_allowed = False
                break

        if is_in_allowed:
            result += 1


    return result

#https://leetcode.com/problems/count-the-number-of-consistent-strings/description/