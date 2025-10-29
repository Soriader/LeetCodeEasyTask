def smallestNumber(n):
    """
    :type n: int
    :rtype: int
    """
    while toBinary(n) == -1:
        n += 1
        toBinary(n)

    return n


def toBinary(n):
    binary_representation = format(n, 'b')

    if all(bit == '1' for bit in binary_representation):
        return n
    else:
        return -1

#https://leetcode.com/problems/smallest-number-with-all-set-bits/description/?envType=daily-question&envId=2025-10-29
