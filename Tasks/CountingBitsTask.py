def countBits(n):
    """
    :type n: int
    :rtype: List[int]
    """
    result = [0, ]
    iterator = 1

    while n >= iterator:
        to_binary = bin(iterator)
        result.append(to_binary.count("1"))
        iterator += 1

    return result
#https://leetcode.com/problems/counting-bits/description/