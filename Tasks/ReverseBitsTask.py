def reverseBits(self, n):
    """
    :type n: int
    :rtype: int
    """
    result = 0

    for i in range(32):
        result <<= 1
        result |= n & 1
        n >>= 1
    return result

#https://leetcode.com/problems/reverse-bits/description/