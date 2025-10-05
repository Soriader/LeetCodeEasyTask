def isSameAfterReversals(self, num):
    """
    :type num: int
    :rtype: bool
    """
    if num == 0:
        return True

    reversed_number = str(num)[::-1]
    final_number = int(reversed_number)

    if (int(str(final_number)[::-1])) == num:
        return True

    return False

#https://leetcode.com/problems/a-number-after-a-double-reversal/description/